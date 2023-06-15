#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose

if __name__ == '__main__':
    rospy.init_node('ur5_cartesian_control_test')
    pub = rospy.Publisher('/ur5_cartesian_pose', Pose, queue_size=10)
    rate = rospy.Rate(10) # 10Hz

    while not rospy.is_shutdown():
        # Crear objeto "Pose" con las coordenadas deseadas
        pose = Pose()
        pose.position.x = 0.5
        pose.position.y = 0.5
        pose.position.z = 0.5
        pose.orientation.w = 1.0 # Orientación arbitraria

        # Publicar el mensaje en el tópico "/ur5_cartesian_pose"
        pub.publish(pose)

        # Esperar antes de publicar el siguiente mensaje
        rate.sleep()

