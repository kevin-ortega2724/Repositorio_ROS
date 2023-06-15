#!/usr/bin/env python3
# encoding: utf-8

import rospy      
import actionlib  
import numpy as np
import math
import random
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from math import pi, atan, atan2, sqrt
from tf.transformations import euler_from_matrix
#from ur_kinematics import forward, inverse

# Definimos las dimensiones de la semiesfera
radio = 10
altura = 20

# Definimos el número de muestras que deseamos tomar
n_muestras = 100

# Definimos una lista vacía para almacenar las coordenadas
coordenadas = []

# Generamos n_muestras de coordenadas aleatorias en la semiesfera
for i in range(n_muestras):
    # Generamos un ángulo aleatorio en el rango de 0 a 2*pi
    angulo = random.uniform(0, 2*math.pi)
    # Generamos una altura aleatoria en el rango de 0 a altura
    z = random.uniform(0, altura)
    # Calculamos el radio de la proyección de las coordenadas en el plano xy
    r = radio * math.sqrt(z / altura)
    # Calculamos las coordenadas x e y
    x = r * math.cos(angulo)
    y = r * math.sin(angulo)
    # Agregamos las coordenadas a la lista
    coordenadas.append((x, y, z))
    x_deseado, y_deseado, z_deseado = coordenadas[i]

# Imprimimos las coordenadas generadas
#print(coordenadas)

# Definimos las dimensiones del manipulador de 6 dof
l1 = 10
l2 = 10
l3 = 10
l4 = 10
l5 = 10
l6 = 10

# Definimos las coordenadas de la posición deseada del efector final
#x_deseado, y_deseado, z_deseado = random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(0, 20)


x_deseado, y_deseado, z_deseado = coordenadas[i]
# Calculamos el ángulo de la base
theta1 = math.atan2(y_deseado, x_deseado)

# Calculamos la proyección en el plano xy del punto de destino
p = math.sqrt(x_deseado**2 + y_deseado**2) - l6*math.cos(theta1)

# Calculamos el ángulo de la primera articulación
theta2 = math.atan2(z_deseado - l1, p) - math.atan2(l3*math.sin(math.acos(l2/l3)), l2 + l3*math.cos(math.acos(l2/l3)))

# Calculamos el ángulo de la segunda articulación
alpha = math.acos(l2/l3)
beta = math.atan2(l3*math.sin(alpha), l2 + l3*math.cos(alpha))
gamma = math.atan2(z_deseado - l1, p)
theta3 = gamma - beta

# Calculamos el ángulo de la tercera articulación
theta4 = math.atan2(-y_deseado*math.cos(theta1) - x_deseado*math.sin(theta1), z_deseado - l1 - l2*math.sin(theta2) - l3*math.sin(theta2 + theta3) - l4)

# Calculamos el ángulo de la cuarta articulación
theta5 = math.acos(math.sin(theta4)*(y_deseado*math.cos(theta1) + x_deseado*math.sin(theta1) + l5)/l4)

# Calculamos el ángulo de la quinta articulación
theta6 = math.atan2(math.sin(theta1)*(math.sin(theta4)*math.cos(theta5)*y_deseado - math.sin(theta4)*math.sin(theta5)*x_deseado + math.cos(theta4)*l4*math.cos(theta5)) - math.cos(theta1)*(z_deseado - l1 - l2*math.sin(theta2) - l3*math.sin(theta2 + theta3) - l4*math.sin(theta4)), -math.cos(theta1)*(math.sin(theta4)*math.cos(theta5)*y_deseado - math.sin(theta4)*math.sin(theta5)*x_deseado + math.cos(theta4)*l4*math.cos(theta5)) - math.sin(theta1)*(z_deseado - l1 - l2*math.sin(theta2) - l3*math.sin(theta2 + theta3) - l4*math.sin(theta4)))

# Imprimimos los ángulos calculados
print(theta1, theta2, theta3, theta4, theta5, theta6)



def generate_joint_positions():
    arm_joint_positions0  = [theta1, theta2, theta3, theta4,theta5, theta6]
    return [arm_joint_positions0]

def generate_joint_names():
    return ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint",
            "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

def generate_trajectory(joint_positions, joint_names, duration):
    trajectory = JointTrajectory()
    trajectory.joint_names = joint_names
    trajectory.points.append(JointTrajectoryPoint())
    trajectory.points[0].positions = joint_positions
    trajectory.points[0].velocities = [0.0] * len(joint_positions)
    trajectory.points[0].accelerations = [0.0] * len(joint_positions)
    trajectory.points[0].time_from_start = rospy.Duration(duration)
    return trajectory

def move_arm():
    rospy.init_node('send_joints')
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)

    rospy.loginfo("Waiting for arm_controller...")
    arm_client = actionlib.SimpleActionClient("arm_controller/follow_joint_trajectory", FollowJointTrajectoryAction)
    arm_client.wait_for_server()
    rospy.loginfo("...connected.")

    arm_joint_positions = generate_joint_positions()
    arm_joint_names = generate_joint_names()

    for joint_positions in arm_joint_positions:
        trajectory = generate_trajectory(joint_positions, arm_joint_names, 1.0)
        arm_client.send_goal(FollowJointTrajectoryGoal(trajectory=trajectory))
        arm_client.wait_for_result()

if __name__ == "__main__":
    move_arm()
    
    
    

