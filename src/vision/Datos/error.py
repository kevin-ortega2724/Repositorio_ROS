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

def image_callback(image_msg):
    # Convert the ROS image to OpenCV format
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw1/img_{}.png".format(date_str) #Cambiar ruta
    ret = cv2.imwrite(filename, cv_image)
    print('pruebaa1')
# Agregar información de la pose al archivo CSV
    with open('/home/ko/ur_ws/src/vision/Datos/capturas/poses.csv', mode='a') as csv_file:
        fieldnames = ['ruta_imagen', 'posicion_x', 'posicion_y', 'posicion_z']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'ruta_imagen': filename, 'posicion_x': '0.0', 'posicion_y': '0.0', 'posicion_z': '0.0'})
    return ret
    
def image_callback2(image_msg):
    # Convert the ROS image to OpenCV format
    bridge1 = CvBridge()
    try:
        cv_image = bridge1.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw2/img_{}.png".format(date_str)
    ret1 = cv2.imwrite(filename, cv_image)
    print('pruebaa2')
    
    return ret1


def image_callback3(image_msg):
    # Convert the ROS image to OpenCV format
    bridge2 = CvBridge()
    try:
        cv_image = bridge2.imgmsg_to_cv2(image_msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    # GUardar imágenes en disco
    timestamp = image_msg.header.stamp
    date_str = datetime.datetime.fromtimestamp(rospy.Time.to_sec(timestamp)).strftime('%H-%M-%S')
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/raw3/img_{}.png".format(date_str)
    ret2 = cv2.imwrite(filename, cv_image)
    print('pruebaa3')
    
    return ret2
 
if __name__ == '__main__':
    rospy.init_node('image_saver', anonymous=True)
    # Suscribo al topic de imagen
    image_sub, image_sub1, image_sub2 = rospy.Subscriber("/camera/color/image_raw", Image, image_callback), rospy.Subscriber("/camera/color/image_raw1", Image, image_callback2), rospy.Subscriber("/camera/color/image_raw2", Image, image_callback3)
    print('Capturando imágenes')
    rospy.spin()

