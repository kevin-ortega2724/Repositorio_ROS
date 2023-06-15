#!/usr/bin/env python3

from gazebo_msgs.msg import ModelState
import rospy
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState
joint_names = ["shoulder_pan_joint"]
def set_model_state_proxy(target_pose, joint_names):
    model_state = ModelState()
    model_state.model_name = "ur5"
    model_state.pose = target_pose
    
    model_state.joint_names = ["shoulder_pan_joint"]

    try:
        set_model_state = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)
        resp = set_model_state(model_state)
        return resp.success
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)
        


# Crear un objeto ModelState y establecer la información de la posición y orientación
target_pose = ModelState()
target_pose.model_name = "ur5"
target_pose.pose.position.x = -0.18680383893593536
target_pose.pose.position.y = 0.8602882478096703
target_pose.pose.position.z = -0.47435056281126575
target_pose.pose.orientation.w = 0.0

# Lista de nombres de articulaciones

# Llamar a la función set_model_state_proxy
set_model_state_proxy(target_pose, joint_names)
