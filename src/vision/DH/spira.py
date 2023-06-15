#!/usr/bin/env python3

import rospy
import csv
import cv2
import os
from sensor_msgs.msg import JointState, Image
from cv_bridge import CvBridge
from control_msgs.msg import JointTrajectoryControllerState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from cv_bridge import CvBridge, CvBridgeError

class CameraSubscriber:
    """Subscribes to a camera topic and publishes the images to another topic."""

    def __init__(self, camera_topic, image_pub):
        self.camera_topic = camera_topic
        self.image_pub = image_pub
        self.bridge = CvBridge()
        self.subscriber = rospy.Subscriber(self.camera_topic, Image, self.callback)

    def callback(self, data):
        try:
            # Convert the image to a NumPy array
            if data.encoding == '32FC1':
                # If the image is a depth image, save it as a NumPy array without conversion
                frame = self.bridge.imgmsg_to_cv2(data, data.encoding)
            else:
                # If the image is an RGB image, convert it to a NumPy array
                frame = self.bridge.imgmsg_to_cv2(data, "bgr8")

            # Publish the image to the image_pub topic
            if data.encoding == '32FC1':
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, data.encoding))
            else:
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
        except cv_bridge.CvBridgeError as e:
            rospy.logerr(e)

def read_csv_file(file_path):
    """Reads a CSV file and returns a list of lists containing the joint angles
    for each point in the file."""
    points = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            angles = [float(num) for num in row[:-1]]
            tstamp = float(row[-1])
            points.append(angles + [tstamp])
    return points
def send_joint_angles(joint_angles):
    """Sends a JointTrajectory message to the robot to control the joint positions."""
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(10)

    # Create the JointTrajectory message
    joint_traj_msg = JointTrajectory()
    joint_traj_msg.header.stamp = rospy.Time.now()
    joint_traj_msg.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                                  'elbow_joint', 'wrist_1_joint',
                                  'wrist_2_joint', 'wrist_3_joint']
    point = JointTrajectoryPoint()
    point.positions = joint_angles
    point.time_from_start = rospy.Duration(1.0)
    joint_traj_msg.points.append(point)

    # Publish the JointTrajectory message
    pub.publish(joint_traj_msg)

    # Wait for the robot to reach the desired position
    state_msg = rospy.wait_for_message('/arm_controller/state', JointTrajectoryControllerState)
    tstamp = state_msg.header.stamp.to_sec()

    # Save the timestamp to the CSV file
    with open('/home/ko/ur_ws/src/vision/Datos/angulos.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([joint_angles[0], joint_angles[1], joint_angles[2], joint_angles[3], joint_angles[4], joint_angles[5], tstamp])

    
def capture_images(joint_angles, counter, output_dir):
    """Captures images from the cameras and saves them as PNG files."""
    # Send the joint angles to the robot and wait for the robot to reach the desired position
    send_joint_angles(joint_angles)
    rospy.sleep(1.0)  # Wait for the robot to settle

    # Get the time of the desired position
    t_desired = rospy.Time.now()

    # Define the output directory for the images
    output_dir_cam1 = output_dir + '/raw1'
    output_dir_cam2 = output_dir + '/raw2'
    output_dir_cam3 = output_dir + '/raw3'
    output_dir_depth1 = output_dir + '/depth1'
    output_dir_depth2 = output_dir + '/depth2'
    output_dir_depth3 = output_dir + '/depth3'

    # Create the output directories if they don't exist
    if not os.path.exists(output_dir_cam1):
        os.makedirs(output_dir_cam1)
    if not os.path.exists(output_dir_cam2):
        os.makedirs(output_dir_cam2)
    if not os.path.exists(output_dir_cam3):
        os.makedirs(output_dir_cam3)
    if not os.path.exists(output_dir_depth1):
        os.makedirs(output_dir_depth1)
    if not os.path.exists(output_dir_depth2):
        os.makedirs(output_dir_depth2)
    if not os.path.exists(output_dir_depth3):
        os.makedirs(output_dir_depth3)

    # Capture images from the cameras and save them as PNG files
    image1 = None
    image2 = None
    image3 = None
    depth1 = None
    depth2 = None
    depth3 = None

    while image1 is None or image2 is None or image3 is None or depth1 is None or depth2 is None or depth3 is None:
        # Capture images from the cameras
        if image1 is None:
            try:
                image1 = rospy.wait_for_message('/camera/color/image_raw', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        if image2 is None:
            try:
                image2 = rospy.wait_for_message('/camera/color/image_raw1', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        if image3 is None:
            try:
                image3 = rospy.wait_for_message('/camera/color/image_raw2', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        # Capture images from the depth cameras
        if depth1 is None:
            try:
                depth1 = rospy.wait_for_message('/camera/depth/image_raw', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        if depth2 is None:
            try:
                depth2 = rospy.wait_for_message('/camera/depth/image_raw1', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        if depth3 is None:
            try:
                depth3 = rospy.wait_for_message('/camera/depth/image_raw2', Image, timeout=1.0)
            except rospy.exceptions.ROSException:
                pass

        # Check if the images were captured at the desired time
        t_image1 = image1.header.stamp if image1 is not None else None
        t_image2 = image2.header.stamp if image2 is not None else None
        t_image3 = image3.header.stamp if image3 is not None else None
        t_depth1 = depth1.header.stamp if depth1 is not None else None
        t_depth2 = depth2.header.stamp if depth2 is not None else None
        t_depth3 = depth3.header.stamp if depth3 is not None else None
        if t_image1 is not None and t_image2 is not None and t_image3 is not None and t_depth1 is not None and t_depth2 is not None and t_depth3 is not None:
            if abs((t_image1 - t_desired).to_sec()) > 0.1 or abs((t_image2 - t_desired).to_sec()) > 0.1 or abs((t_image3 - t_desired).to_sec()) > 0.1 or abs((t_depth1 - t_desired).to_sec()) > 0.1 or abs((t_depth2 - t_desired).to_sec()) > 0.1 or abs((t_depth3 - t_desired).to_sec()) > 0.1:
                image1 = None
                image2 = None
                image3 = None
                depth1 = None
                depth2 = None
                depth3 = None
            else:
                # Convert the images to NumPy arrays
                bridge = CvBridge()
                frame1 = bridge.imgmsg_to_cv2(image1, "bgr8")
                frame2 = bridge.imgmsg_to_cv2(image2, "bgr8")
                frame3 = bridge.imgmsg_to_cv2(image3, "bgr8")
                depth_frame1 = bridge.imgmsg_to_cv2(depth1)
                depth_frame2 = bridge.imgmsg_to_cv2(depth2)
                depth_frame3 = bridge.imgmsg_to_cv2(depth3)
                #depth_array1 = np.array(depth_frame1, dtype=np.float32)
                #depth_array2 = np.array(depth_frame2, dtype=np.float32)
                #depth_array3 = np.array(depth_frame3, dtype=np.float32)

                # Escalar la matriz de profundidad para convertirla en una imagen de 8 bits
                #depth_array_scaled1 = cv2.normalize(depth_array1, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                #depth_array_scaled2 = cv2.normalize(depth_array2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                #depth_array_scaled3 = cv2.normalize(depth_array3, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

                # Save the images as PNG files
                filename1 = output_dir_cam1 + '/image{}.png'.format(counter)
                filename2 = output_dir_cam2 + '/image{}.png'.format(counter)
                filename3 = output_dir_cam3 + '/image{}.png'.format(counter)
                depth_filename1 = output_dir_depth1 + '/depth{}.png'.format(counter)
                depth_filename2 = output_dir_depth2 + '/depth{}.png'.format(counter)
                depth_filename3 = output_dir_depth3 + '/depth{}.png'.format(counter)    
                cv2.imwrite(filename1, frame1)
                cv2.imwrite(filename2, frame2)
                cv2.imwrite(filename3, frame3)
                cv2.imwrite(depth_filename1, depth_frame1)
                cv2.imwrite(depth_filename2, depth_frame2)
                cv2.imwrite(depth_filename3, depth_frame3)
                

                rospy.loginfo('Captured images for joint angles: {}'.format(joint_angles))

                # Return True to indicate that the images were captured successfully
                return True

        # Return False to indicate that the images were not captured successfully
        return False
  
  
if __name__ == '__main__':

    # Initialize the ROS node and publishers
    rospy.init_node('ur5_controller')
    pub_joint = rospy.Publisher('/joint_states', JointState, queue_size=10)
    image_pub1 = rospy.Publisher('/camera/color/image_raw1', Image, queue_size=10)
    image_pub2 = rospy.Publisher('/camera/color/image_raw2', Image, queue_size=10)
    image_pub3 = rospy.Publisher('/camera/color/image_raw3', Image, queue_size=10)
    depth_pub1 = rospy.Publisher('/camera/depth/image_raw1', Image, queue_size=10)
    depth_pub2 = rospy.Publisher('/camera/depth/image_raw2', Image, queue_size=10)
    depth_pub3 = rospy.Publisher('/camera/depth/image_raw3', Image, queue_size=10)
    cam_sub1 = CameraSubscriber('/camera/color/image_raw', image_pub1)
    cam_sub2 = CameraSubscriber('/camera/color/image_raw1', image_pub2)
    cam_sub3 = CameraSubscriber('/camera/color/image_raw2', image_pub3)
    depth_sub1 = CameraSubscriber('/camera/depth/image_raw', depth_pub1)
    depth_sub2 = CameraSubscriber('/camera/depth/image_raw1', depth_pub2)
    depth_sub3 = CameraSubscriber('/camera/depth/image_raw2', depth_pub3)
    
    # Read the joint angles from the CSV file
    file_path = "/home/ko/ur_ws/src/vision/Datos/angulos.csv"
    joint_angles_list = read_csv_file(file_path)

    output_dir = "/home/ko/ur_ws/src/vision/Datos"

    # Publish the joint angles and capture images and videos at each position
    counter = 1
    for joint_angles in joint_angles_list:
        rospy.loginfo('Sending joint angles: {}'.format(joint_angles))
        # Capture images from the cameras and save them as PNG files
        while not capture_images(joint_angles, counter, output_dir):
            # If the images were not captured successfully, try again
            pass

        # Move to the next pose only if the images were captured successfully
        counter += 1

    rospy.loginfo('Finished capturing images and videos for all joint angles.')
