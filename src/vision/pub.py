#!/usr/bin/python3
#
#Mensajes ur5
#


import rospy
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import GetModelStateRequest

rospy.init_node('get_end_effector_pose')

client = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
request = GetModelStateRequest()
request.model_name = 'ur5'

response = client(request)

if response.success:
    position = response.pose.position
    orientation = response.pose.orientation

    print("Posición del efector final: ({}, {}, {})".format(position.x, position.y, position.z))
    print("Orientación del efector final: ({}, {}, {})".format(orientation.x, orientation.y, orientation.z))
else:
    print("No se pudo obtener el estado del modelo")

