#!/usr/bin/env python3

"""
Este archivo realiza la operación inversa a la cinemática, obteniendo como entrada los parámetros x, y y z.
Autor @Kevin Ortega
Universidad Tecnológica de Pereira
Ingeniería eléctrica
"""

import numpy as np
from scipy.optimize import minimize
import rospy
from geometry_msgs.msg import Pose
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from mpl_toolkits.mplot3d import Axes3D 


# Generar puntos aleatorios en la parte superior de la esfera 
N = 1000
phi = np.random.uniform(0, np.pi / 2, N)
theta = np.random.uniform(0, 2 * np.pi, N)
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Función que define la cinemática directa del robot UR5
def forward_kinematics(angles):
    # Matrices de transformación para cada articulación del Robor UR5
    T1 = np.array([[np.cos(angles[0]), -np.sin(angles[0]), 0, 0],
                   [np.sin(angles[0]), np.cos(angles[0]), 0, 0],
                   [0, 0, 1, 0.089159],
                   [0, 0, 0, 1]])
    T2 = np.array([[np.cos(angles[1]), 0, np.sin(angles[1]), 0.28],
                   [0, 1, 0, 0],
                   [-np.sin(angles[1]), 0, np.cos(angles[1]), 0],
                   [0, 0, 0, 1]])
    T3 = np.array([[np.cos(angles[2]), -np.sin(angles[2]), 0, 0.13585],
                   [np.sin(angles[2]), np.cos(angles[2]), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    T4 = np.array([[np.cos(angles[3]), 0, np.sin(angles[3]), 0.0],
                   [0, 1, 0, -0.1197],
                   [-np.sin(angles[3]), 0, np.cos(angles[3]), 0.495],
                   [0, 0, 0, 1]])
    T5 = np.array([[np.cos(angles[4]), -np.sin(angles[4]), 0, 0],
                   [np.sin(angles[4]), np.cos(angles[4]), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    T6 = np.array([[np.cos(angles[5]), 0, np.sin(angles[5]), 0],
                   [0, 1, 0, 0],
                   [-np.sin(angles[5]), 0, np.cos(angles[5]), 0.0823],
                   [0, 0, 0, 1]])

    # Cálculo de la matriz de transformación total 
    T = T1.dot(T2).dot(T3).dot(T4).dot(T5).dot(T6)

    # Cálculo de la posición final en el espacio
    x_pos = T[0, 3]
    y_pos = T[1, 3]
    z_pos = T[2, 3]

    return x_pos, y_pos, z_pos


# Función que define la cinemática inversa del robot UR5
def inverse_kinematics(target_position):
    # Definir la función objetivo que minimiza la distancia entre la posición objetivo y la posición actual
    def distance_to_target(angles):
        x_pos, y_pos, z_pos = forward_kinematics(angles)
        return np.linalg.norm(np.array([x_pos, y_pos, z_pos]) - target_position)

    # Resolución del problema de optimización utilizando un algoritmo de búsqueda
    initial_angles = np.zeros(6)
    result = minimize(distance_to_target, initial_angles)

    # Devolver los ángulos resultantes
    return result.x


# Calcular los ángulos necesarios para alcanzar la posición objetivo
angles = inverse_kinematics([x[0], y[0], z[0]])
print(angles)
angles1 = inverse_kinematics([x[1], y[1], z[1]])
print(angles1)  # angulos de la cinemática inversa

waypoints = [angles, [0, 0, 0, 0, 0.3, 1.20]]  # Puntos iniciales


def main():
    rospy.init_node('send_joints')
    pub = rospy.Publisher('/arm_controller/command',
                          JointTrajectory,
                          queue_size=10)

    # Create the topic message
    traj = JointTrajectory()
    traj.header = Header()
    # Joint names for UR5
    traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                        'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
                        'wrist_3_joint']  #Articulaciones del brazo UR5

    rate = rospy.Rate(1) 
    cnt = 0
    pts = JointTrajectoryPoint()
    traj.header.stamp = rospy.Time.now()

    while not rospy.is_shutdown():
        cnt += 1

        if cnt % 2 == 1:
            pts.positions = waypoints[0]
        else:
            pts.positions = waypoints[1]

        pts.time_from_start = rospy.Duration(1.0)

        # Set the points to the trajectory
        traj.points = []
        traj.points.append(pts)
        # Publish the message
        pub.publish(traj)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
