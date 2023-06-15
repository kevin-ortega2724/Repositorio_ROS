#!/usr/bin/env python3

import rospy
import time
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def move_ur5(x, y, z):
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('my_ur5_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    joint_state = JointState()
    joint_state.header = Header()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
    joint_state.position = [0, -1.57, 1.57, 0, 0, 0]
    joint_state.velocity = []
    joint_state.effort = []

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        pub.publish(joint_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_ur5(0.5, 0, 0.2)
    except rospy.ROSInterruptException:
        pass

