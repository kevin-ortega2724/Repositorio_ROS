#!/usr/bin/env python3

from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import rospy

def is_point_valid(point, set_model_state_proxy, get_model_state_proxy):
    model_state = ModelState()
    model_state.model_name = "ur5"

    # Posición y orientación
    
    model_state.pose = Pose()
    model_state.pose.position.x = point[0]
    model_state.pose.position.y = point[0]
    model_state.pose.position.z = point[0]
    model_state.pose.orientation.x = -45
    model_state.pose.orientation.y = 3
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

# Inicializar ROS
rospy.init_node("check_collision_node")

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

