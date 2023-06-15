#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def depth_callback(image_msg):
    # Convertir la imagen de profundidad a una matriz NumPy
    bridge = CvBridge()
    depth_image = bridge.imgmsg_to_cv2(image_msg)
    depth_array = np.array(depth_image, dtype=np.float32)

    # Escalar la matriz de profundidad para convertirla en una imagen de 8 bits
    depth_array_scaled = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Guardar la imagen en formato JPEG
    filename = "/home/ko/ur_ws/src/vision/Datos/capturas/deep/img_{}.png"
    cv2.imwrite(filename, depth_array_scaled)

if __name__ == '__main__':
    rospy.init_node('depth_saver', anonymous=True)
    depth_sub = rospy.Subscriber("/camera/depth/image_raw", Image, depth_callback)
    rospy.spin()

