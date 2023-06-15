#!/usr/bin/env python3

import rospy
import csv
import sys
from sensor_msgs.msg import JointState

def read_csv_file(file_path):
    """Reads a CSV file and returns a list of lists containing the joint angles
    for each point in the file."""
    points = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            angles = [float(num) for num in row]
            points.append(angles)
    return points

if __name__ == '__main__':
    # Initialize the ROS node and publisher
    rospy.init_node('csv_reader')
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10)

    # Read the joint angles from the CSV file
    file_path = "/home/ko/ur_ws/src/vision/Datos/angulos.cvs"
    joint_angles_list = read_csv_file(file_path)

    # Create the JointState message
    joint_state_msg = JointState()
    joint_state_msg.header.stamp = rospy.Time.now()
    joint_state_msg.name = ['shoulder_pan_joint', 'shoulder_lift_joint',
                            'elbow_joint', 'wrist_1_joint',
                            'wrist_2_joint', 'wrist_3_joint']

    # Publish the joint angles as JointState messages
    for joint_angles in joint_angles_list:
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.position = joint_angles
        pub.publish(joint_state_msg)
        rate.sleep()

    rospy.loginfo('Finished publishing all joint states.')

