#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from geometry_msgs.msg import Point # importa Point desde geometry_msgs
class ImageGrabber:
    def __init__(self):
        self.bridge = CvBridge()
        self.image1 = None
        self.image2 = None
        self.image3 = None
        rospy.Subscriber('/camera1/image_raw', Image, self.callback1)
        rospy.Subscriber('/camera2/image_raw', Image, self.callback2)
        rospy.Subscriber('/camera3/image_raw', Image, self.callback3)
        self.robot_position = None
        rospy.Subscriber('/robot_position', Point, self.position_callback) # suscribe al tópico de la posición del robot
        
    def position_callback(self, data):
        x = data.x
        y = data.y
        z = data.z
        # verifica si el robot ha alcanzado la posición deseada utilizando la lógica específica de tu aplicación
        
    def callback1(self, data):
        if robot_has_reached_desired_position:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image1 = cv_image
        
    def callback2(self, data):
        if robot_has_reached_desired_position:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image2 = cv_image
        
    def callback3(self, data):
        if robot_has_reached_desired_position:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image3 = cv_image

if __name__ == '__main__':
    rospy.init_node('image_grabber')
    ig = ImageGrabber()
    rospy.sleep(10) # espera 10 segundos para capturar imágenes
    # realiza la operación de procesamiento de imágenes aquí
    # por ejemplo, la reconstrucción de una imagen tridimensional usando las imágenes almacenadas en ig.image1, ig.image2 y ig.image3



