#!/usr/bin/env python3

import rospy
import cv2


from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
print('inicio por lo menos')
class Camera:

	def __init__(self):

		self.publisher = rospy.Publisher('camera_link', Image, queue_size = 10)
		self.img = cv2.imread("/home/ko/ur_ws/src")
		self.bridge = CvBridge()

	def publish_image(self):
		image = self.bridge.cv2_to_imgmsg(self.img, encoding = "passthrough")
		self.publisher.publish(image)
		print("Se publico Imagen")


if __name__ =='__main__':
	try:
		rospy.init_node('camera_node')
		rate = rospy.Rate(10)

		cam = Camera()

		while not rospy.is_shutdown():
			cam.publish_image
			rate.sleep()
	except rospy.ROSInterruptException:
		pass
