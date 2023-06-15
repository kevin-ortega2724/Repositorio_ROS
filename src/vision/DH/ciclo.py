import rospy
import numpy as np
import time
from std_msgs.msg import Header
from sensor_msgs.msg import JointState

# Inicializar el nodo de ROS
rospy.init_node("controlador_ur5")

# Definir las dimensiones del brazo UR5
a = [0.0, -0.425, -0.39225, 0.0, 0.0, 0.0]
d = [0.089159, 0.0, 0.0, 0.10915, 0.09465, 0.0823]

# Definir las coordenadas objetivo
x = 0.3
y = 0.3
z = 0.3

# Calcular los ángulos de las articulaciones utilizando la cinemática inversa
# (rellenar con tu código para la cinemática inversa)
theta1 = 0.0
theta2 = 0.0
theta3 = 0.0
theta4 = 0.0
theta5 = 0.0
theta6 = 0.0

# Crear un mensaje de tipo JointState con los ángulos de las articulaciones del brazo
header = Header()
header.stamp = rospy.Time.now()
joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
joint_positions = [theta1, theta2, theta3, theta4, theta5, theta6]
joint_state_msg = JointState(header=header, name=joint_names, position=joint_positions)

# Publicar el mensaje de JointState en el tópico /joint_states para controlar el brazo
joint_state_publisher = rospy.Publisher("/joint_states", JointState, queue_size=1)
while not rospy.is_shutdown():
    joint_state_publisher.publish(joint_state_msg)
    time.sleep(0.01)

