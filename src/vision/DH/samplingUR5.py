#!/usr/bin/env python3

from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import SetModelState
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
#from gazebo_msgs.msg import Twist
import rospy
import random
import math
import gazebo_msgs.srv
import gazebo_msgs.msg
import geometry_msgs.msg
from gazebo_msgs.srv import GetJointProperties
#from controller_manager_msgs.srv import GetJointProperties
joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
def get_joint_properties_proxy(joint_name):
    rospy.wait_for_service('/gazebo/get_joint_properties')
    try:
        get_joint_properties = rospy.ServiceProxy('/gazebo/get_joint_properties', GetJointProperties)
        response = get_joint_properties(joint_names)
        return response
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)
       

        
def is_point_valid(point, set_model_state_proxy, get_model_state_proxy):
    model_state = ModelState()
    model_state.model_name = "ur5"

    # Posición y orientación
    
    model_state.pose = Pose()
    model_state.pose.position.x = point[0]
    model_state.pose.position.y = point[1]
    model_state.pose.position.z = point[2]
    model_state.pose.orientation.x = -5.0
    model_state.pose.orientation.y = 3.6
    model_state.pose.orientation.z = 0.4
    model_state.pose.orientation.w = -1.5

    # Velocidad lineal y angular
    
    model_state.twist = Twist()
    model_state.twist.linear.x = 0.0
    model_state.twist.linear.y = 0.0
    model_state.twist.linear.z = 0.0
    model_state.twist.angular.x = 0.0
    model_state.twist.angular.y = 0.0
    model_state.twist.angular.z = 0.0

    # Frame de referencia
    model_state.reference_frame = "" # Puedes dejar esto en blanco si deseas usar el frame por defecto

    # Setear el estado del modelo
    set_model_state_proxy(model_state)

    # Verificar si el punto es válido
    try:
        set_model_state_proxy(model_state)
        print("El objeto ModelState se acopló correctamente en la función set_model_state_proxy")
    except TypeError as e:
        print("Hubo un error al acoplar el objeto ModelState:", e)

    return True # o False si el punto no es válido



def control_robot(point, set_model_proxy, get_model_proxy):
    # Controlar el robot hacia el punto especificado en Gazebo
    current_state = get_model_proxy("ur5", "world").pose
    
    # Obtener el estado de los joint
    get_joint_properties = rospy.ServiceProxy('/gazebo/get_joint_properties', GetJointProperties)
    joint_properties = get_joint_properties('ur5::shoulder_pan_joint')
    joint_positions = [joint_properties.position]
    joint_names = ['shoulder_pan_joint']

    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = current_state.position.x + point[0]
    target_pose.position.y = current_state.position.y + point[1]
    target_pose.position.z = current_state.position.z + point[2]
    target_pose.orientation = current_state.orientation
    
    set_model_proxy("ur5", target_pose, joint_names, joint_positions)   



def sample_point_on_sphere():
    theta = 2 * math.pi * random.random()
    phi = math.acos(2 * random.random() - 1)
    x = math.sin(phi) * math.cos(theta)
    y = math.sin(phi) * math.sin(theta)
    z = math.cos(phi)
    return x, y, z

if __name__ == '__main__':
    rospy.init_node('ur5_sampler')
    
    rospy.wait_for_service('/gazebo/set_model_configuration')
    set_model_config_proxy = rospy.ServiceProxy('/gazebo/set_model_configuration', gazebo_msgs.srv.SetModelConfiguration)
    
    rospy.wait_for_service('/gazebo/set_model_state')
    set_model_state_proxy = rospy.ServiceProxy('/gazebo/set_model_state', gazebo_msgs.srv.SetModelState)
    
    rospy.wait_for_service('/gazebo/get_model_state')
    get_model_state_proxy = rospy.ServiceProxy('/gazebo/get_model_state', gazebo_msgs.srv.GetModelState)
    
		# Inicializar el proxy de SetModelState
    set_model_state_proxy = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)
    set_model_state_proxy.wait_for_service()

    # Inicializar el proxy de GetModelState (opcional, dependiendo de tus necesidades)
    get_model_state_proxy = rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
    get_model_state_proxy.wait_for_service()

   # Probar la función con algún punto de prueba
    point = (-0.18680383893593536, 0.8602882478096703, -0.47435056281126575)
    if is_point_valid(point, set_model_state_proxy, get_model_state_proxy):
        print("El punto es válido")
    else:
        print("El punto no es válido")
    
    while not rospy.is_shutdown():
        point = (-0.18680383893593536, 0.8602882478096703, -0.47435056281126575)
        if is_point_valid(point, set_model_state_proxy, get_model_state_proxy):
        
            control_robot(point, set_model_state_proxy, get_model_state_proxy)
            rospy.loginfo("Moved to a new valid position")
        else:
            rospy.logwarn("Invalid point, trying again")

