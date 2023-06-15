#!/usr/bin/env python3

"""
Este archivo pretende guardar las imágenes necesarias según el tópico deseado utilizando librerias de ROS
Autor @Kevin Ortega
Universidad Tecnológica de Pereira
Ingeniería eléctrica
"""

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import datetime
import cv2
import csv
from std_msgs.msg import Bool
import math
import random
import numpy as np
import rospy
import svgwrite
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pi = math.pi

# Ángulos para cada articulación del robot
angles = [i * pi/4 for i in range(13)]
angles1 = [-2.5132741228718345, -2.303834612632515, -2.0943951023931957, -1.884955592153876, -1.6755160819145565, -1.4660765716752369, -1.2566370614359172, -1.0471975511965979, -0.8377580409572782]
angles2 = [-2.00, -2.0943951023931953, -1.832595714594046, -1.5707963267948966, -1.308996938995747, 2.00, 2.0943951023931953, 1.832595714594046, 1.5707963267948966, 1.308996938995747]

# Combinaciones de ángulos para cada articulación
combinations = [(a, b, c, random.uniform(-3.490658503988659
, 0.87266), random.uniform(-1.7453292519943295
, -2.6117), random.uniform(0, pi)) for a in angles for b in angles1 for c in angles2]
combinations_list = [list(pair) for pair in combinations]
waypoints = combinations_list
i = 0


def image_callback(image_msg):

    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
        #image_sub = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
        #print('Capturando imágenes', pts.positions)
    # Convert the ROS image to OpenCV format
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw1/img_{}.png".format(i)
    ret = cv2.imwrite(filename, cv_image)
    #print('pruebaa1')


    return ret
    
def depth_callbacka(image_msg):
    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
    # Convertir la imagen de profundidad a una matriz NumPy
    bridgea = CvBridge()
    depth_image = bridgea.imgmsg_to_cv2(image_msg)
    depth_array = np.array(depth_image, dtype=np.float32)

    # Escalar la matriz de profundidad para convertirla en una imagen de 8 bits
    depth_array_scaled = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Guardar la imagen en formato JPEG
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filenamea = "/home/ko/ur_ws/src/vision/Datos/capturas/depth1/img_{}.png".format(i)
    cv2.imwrite(filenamea, depth_array_scaled)
    
    
def image_callback2(image_msg):
    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
    # Convert the ROS image to OpenCV format
    bridge1 = CvBridge()
    try:
        cv_image = bridge1.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw2/img_{}.png".format(i)
    ret1 = cv2.imwrite(filename, cv_image)

    
    return ret1  

def depth_callbackb(image_msg):
    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
    # Convertir la imagen de profundidad a una matriz NumPy
    bridgeb = CvBridge()
    depth_image = bridgeb.imgmsg_to_cv2(image_msg)
    depth_array = np.array(depth_image, dtype=np.float32)

    # Escalar la matriz de profundidad para convertirla en una imagen de 8 bits
    depth_array_scaled = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Guardar la imagen en formato JPEG
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filenameb = "/home/ko/ur_ws/src/vision/Datos/capturas/depth2/img_{}.png".format(i)
    cv2.imwrite(filenameb, depth_array_scaled)
    

def image_callback3(image_msg):
    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
    # Convert the ROS image to OpenCV format
    bridge2 = CvBridge()
    try:
        cv_image = bridge2.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw3/img_{}.png".format(i)
    ret2 = cv2.imwrite(filename, cv_image)
 
    
    return ret2

def depth_callbackc(image_msg):
    while rospy.is_shutdown():
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
    # Convertir la imagen de profundidad a una matriz NumPy
    bridgec = CvBridge()
    depth_image = bridgec.imgmsg_to_cv2(image_msg)
    depth_array = np.array(depth_image, dtype=np.float32)

    # Escalar la matriz de profundidad para convertirla en una imagen de 8 bits
    depth_array_scaled = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Guardar la imagen en formato JPEG
    #timestamp = image_msg.header.stamp
    #date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    tstamp = rospy.get_rostime()
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
    filenamec = "/home/ko/ur_ws/src/vision/Datos/capturas/depth3/img_{}.png".format(i)
    cv2.imwrite(filenamec, depth_array_scaled)

if __name__ == '__main__':

    rospy.init_node('send_joints', anonymous=True)
    # Publicador de las trayectorias
    pub = rospy.Publisher('/arm_controller/command',
                          JointTrajectory,
                          queue_size=10)
                          
    traj = JointTrajectory()
    traj.header = Header()
    traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                        'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
                        'wrist_3_joint']
    rate = rospy.Rate(1)
    pts = JointTrajectoryPoint()
 
    fieldnames = ['ruta_imagen1', 'ruta_imagen2', 'ruta_imagen3', 'theta_i', 'tstamp']
    with open('/home/ko/ur_ws/src/vision/Datos/capturas/posestime1.csv', mode='a',newline='') as csv_file:
            
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
    while not rospy.is_shutdown():
    	
        pts.positions = waypoints[i]
        pts.time_from_start = rospy.Duration(1.1)
        traj.points = [pts]
        pub.publish(traj)
        rate.sleep()

        i = (i + 1) % len(waypoints)
        pub.publish(traj)
        filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw1/img_{}.png".format(i) 
        filename1 = "/home/ko/ur_ws/src/vision/Datos/capturas/raw2/img_{}.png".format(i) 
        filename2 = "/home/ko/ur_ws/src/vision/Datos/capturas/raw3/img_{}.png".format(i) 
        filenamea = "/home/ko/ur_ws/src/vision/Datos/capturas/depth1/img_{}.png".format(i) 
        filenameb = "/home/ko/ur_ws/src/vision/Datos/capturas/depth2/img_{}.png".format(i) 
        filenamec = "/home/ko/ur_ws/src/vision/Datos/capturas/depth3/img_{}.png".format(i) 
        #fieldnames = ['ruta_imagen1', 'ruta_imagen2', 'ruta_imagen3', 'theta_i']
# Agregar información de la pose al archivo CSV
        with open('/home/ko/ur_ws/src/vision/Datos/capturas/posestime1.csv', mode='a',newline='') as csv_file:
            tstamp = rospy.get_rostime()
            date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(tstamp)).strftime('%H:%M:%S')
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            #writer.writeheader()
            writer.writerow({'ruta_imagen1': filename, 'ruta_imagen2': filename1, 'ruta_imagen3': filename2, 'theta_i': pts.positions, 'tstamp': date_str})
            rate.sleep()

        #print(pts.positions)
        image_sub, image_sub1, image_sub2,depth_sub, depth_sub1, depth_sub2 = rospy.Subscriber("/camera/color/image_raw", Image, image_callback), rospy.Subscriber("/camera/color/image_raw1", Image, image_callback2), rospy.Subscriber("/camera/color/image_raw2", Image, image_callback3), rospy.Subscriber("/camera/depth/image_raw", Image, depth_callbacka), rospy.Subscriber("/camera/depth/image_raw1", Image, depth_callbackb), rospy.Subscriber("/camera/depth/image_raw2", Image, depth_callbackc)
	

        print('Capturando imágenes',i, pts.positions, date_str)
        

    rospy.spin()

