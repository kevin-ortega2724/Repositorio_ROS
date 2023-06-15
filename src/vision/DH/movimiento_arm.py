#!/usr/bin/env python3
# encoding: utf-8

import rospy      
import actionlib  
import numpy as np
import math
import random
from math import atan2, sqrt, pi
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


"""
Cinemáticas del UR5.

"""
import math

import numpy as np
def micinematica(theta):
    # Definir los valores de los parámetros DH para el robot UR5
    a = [0, -0.425, -0.39225, 0, 0, 0]
    alpha = [-np.pi/2, 0, 0, -np.pi/2, np.pi/2, 0]
    d = [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
    # theta = [0, 0, 0, 0, 0, 0]

    # Definir la matriz de transformación homogénea para cada articulación
    T = [np.array([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(theta[i])*np.sin(alpha[i]), a[i]*np.cos(theta[i])],
                   [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
                   [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
                   [0, 0, 0, 1]]) for i in range(6)]

    # Calcular la matriz de transformación homogénea para la posición y orientación actual de la herramienta final del robot
    T_total = T[0].dot(T[1]).dot(T[2]).dot(T[3]).dot(T[4]).dot(T[5])
    # # Obtener los valores de posición y orientación del efector final
    # p = T_06[:3, 3]
    # R = T_06[:3, :3]
    # print("Valores de posición: ", p)
    # print("Valores de orientación: \n", R)
    # print("T06", T_total)

    #Cinemática Inversa.............
    #Para theta1
    # PO5 = T_total*[0,
    #                0,
    #                -d[5],
    #                1]
    # print("Traslación 0P5",PO5[1,3])
    #Ahora, calculamos para thethe1, así:
    T_5 = T[0].dot(T[1]).dot(T[2]).dot(T[3]).dot(T[4])
    # print("T_5",T_5)
    # print("0T5",T_5[1,3], T_5[0,3])
    t1d = math.atan2(T_5[1,3],T_5[0,3]) + math.acos(d[3] / (math.sqrt(T_5[1,3] ** 2 + T_5[0,3] ** 2))) + math.pi / 2
    t1i = math.atan2(T_5[1,3],T_5[0,3]) - math.acos(d[3] / (math.sqrt(T_5[1,3] ** 2 + T_5[0,3] ** 2))) + math.pi / 2
    # print("Valores posibles de Theta1: ", t1d, t1i)

    #Para theta5
    # Calcular el valor de theta5
    arg = (T_total[0,3]*math.sin(t1d)-T_total[1,3]*math.cos(t1d)-d[3]) / d[5]
    argz = np.clip(arg, -1.0, 1.0)  # Restringir el valor del argumento al rango válido
    t5d = math.acos(argz)

    arg1 = (T_total[0,3]*math.sin(t1d)-T_total[1,3]*math.cos(t1d)-d[3]) / d[5]
    argx = np.clip(arg1, -1.0, 1.0)  # Restringir el valor del argumento al rango válido

    t5i = -math.acos(argx)

    # print("Valores posibles para theta5:", t5d, t5i) #Solo derecha de theta5

    # mag = abs(T_total[1,3]-d[3])
    # print("Tiene que ser menos o igual a d6",mag)

    #Para theta 6

    if math.sin(t5d) != 0:
        t61 = (-T_total[1,0]*math.sin(t1d) + T_total[1,1]*math.cos(t1d)) / math.sin(t5d)
        t62 = (T_total[0,0]*math.sin(t1d) - T_total[0,1]*math.cos(t1d)) / math.sin(t5d)
        t6 = math.atan2(t61, t62)
        # print("Valor theta6: ", t6)
    else:
        print('Indeterminación')




    #Para Theta 3
    T14 = T[1].dot(T[2]).dot(T[3]) #Del fotograma 1 al 4
    # print("T14", T14)


    t3d = (math.acos(math.sqrt(T14[2,3] ** 2 + T14[0,3]**2)**2 - a[1] ** 2 - a[2] ** 2) / (2*a[1] * a[2]))
    t3i = -(math.acos(math.sqrt(T14[2,3] ** 2 + T14[0,3]**2)**2 - a[1] ** 2 - a[2] ** 2) / (2*a[1] * a[2]))

    # print("Valores de theta3", t3d,t3i)


    #Para theta 2

    t2 = math.atan2(-T14[2,3],-T14[0,3]) - math.sin(a[2]*math.sin(t3d)/(math.sqrt(T14[2,3] ** 2 + T14[0,3]**2)))
    # print("Valor theta2", t2)



    #Para theta 4

    T34 = T[2].dot(T[3]) #Del fotograma 3 al 4

    t4 = math.atan2(T34[0,1],T34[0,0])
    # print("Valore theta4", t4)

    lista = [t1d, t1i, t2, t3d, t3i, t4, t5d, t5i, t6]
    # print(lista)
    listad = [t1d, t2, t3d, t4, t5d, t6]
    # print("Solo los de la derecha", listad)
    listai = [t1i, t2, t3i, t4, t5i, t6]
    # print(listai)

    return listai

# Calcular la matriz de transformación homogénea para la configuración actual del robot
T_total = micinematica([-0.5, -0.5, 0, 0, 0, -0.6])

# Calcular los valores posibles de theta1 y theta5

#print("Valores theta: ", T_total)



def generate_joint_positions():
    arm_joint_positions0  = [2.7206801994364183,-0.20943747411287153,0.03412421924792889,-1.5707963267948966,2.7206801994364223,6.123233995736767e-17]
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
    
    
    

