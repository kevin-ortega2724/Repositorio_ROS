#!/usr/bin/python3

import math
import random
import csv
import numpy as np
import rospy
import svgwrite
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pi = math.pi

# Ángulos para cada articulación del robot
angles = [i * pi/4 for i in range(13)]
angles1 = [-2.5132741228718345, -2.303834612632515, -2.0943951023931957, -1.884955592153876, -1.6755160819145565, -1.4660765716752369, -1.2566370614359172, -1.0471975511965979, -0.8377580409572782]
angles2 = [-2.00, -2.0943951023931953, -1.832595714594046, -1.5707963267948966, -1.308996938995747, 2.00, 2.0943951023931953, 1.832595714594046, 1.5707963267948966, 1.308996938995747]

# Combinaciones de ángulos para cada articulación
combinations = [(a, b, c, random.uniform(0, 180), random.uniform(0, 180), random.uniform(0, 180)) for a in angles for b in angles1 for c in angles2]
combinations_list = [list(pair) for pair in combinations]
waypoints = combinations_list

VERBOSE = False


def main():
    rospy.init_node('send_joints')

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
    i = 0
    

    # Guardar los datos en un archivo CSV
    with open('/home/ko/ur_ws/src/vision/Datos/capturas/waypoints.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint'])
	
        while not rospy.is_shutdown():
            pts.positions = waypoints[i]
            pts.time_from_start = rospy.Duration(1.0)
            traj.points = [pts]
            pub.publish(traj)
            rate.sleep()

            i = (i + 1) % len(waypoints)
            pub.publish(traj)
            rate.sleep()
            print(pts.positions,i)

            writer.writerow(pts.positions)
		


if __name__ == '__main__':
    
    try:     
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")

