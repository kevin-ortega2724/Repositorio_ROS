#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray
from ur_kinematics import forward_kinematics, inverse

class UR5Controller:
    def __init__(self):
        self.pub = rospy.Publisher('/ur5/arm_controller/command', Float64MultiArray, queue_size=10)
        self.sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.callback)

    def callback(self, data):
        # Obtener las coordenadas x, y, y z del efector final
        x = data.pose[1].position.x
        y = data.pose[1].position.y
        z = data.pose[1].position.z

        # Calcular las coordenadas angulares del efector final
        # Transformar las coordenadas del efector final al sistema de coordenadas de la base del robot
        position = [x, y, z]
        orientation = [0, 0, 0, 1]  # La orientación del efector final se asume como una orientación estándar
        joint_positions = inverse(position, orientation)

        # Publicar las coordenadas angulares
        self.pub.publish(Float64MultiArray(data=joint_positions))

if __name__ == '__main__':
    rospy.init_node('ur5_controller')
    ur5 = UR5Controller()
    rospy.spin()


