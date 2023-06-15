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

def image_callback(image_msg):
    # Convierto la imagen de ROS a formato OpenCV
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # Guardo la imagen en disco
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw1/img_{}.png".format(date_str)
    cv2.imwrite("filename.png", cv_image)

#Llamo otra función para el otro tópico
def image_callback1(image_msg):
    # Convierto la imagen de ROS a formato OpenCV
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # Guardo la imagen en disco
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename1 = "/home/ko/ur_ws/src/vision/Datos/capturas/raw2/img_{}.png".format(date_str)
    cv2.imwrite("filename1.png", cv_image)
    
#Llamo otra función para el otro tópico
def image_callback2(image_msg):
    # Convierto la imagen de ROS a formato OpenCV
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # Guardo la imagen en disco
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename2 = "/home/ko/ur_ws/src/vision/Datos/capturas/raw3/img_{}.png".format(date_str)
    cv2.imwrite("filename2.png", cv_image)

if __name__ == '__main__':
    rospy.init_node('image_saver', anonymous=True)
    # Suscribo al topic de imagen
    image_sub = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    image_sub1 = rospy.Subscriber("/camera/color/image_raw1", Image, image_callback1)
    image_sub2 = rospy.Subscriber("/camera/color/image_raw2", Image, image_callback2)
    print('Capturando imágenes')
    rospy.spin()

