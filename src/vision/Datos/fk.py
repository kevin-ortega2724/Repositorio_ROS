import numpy as np
import math


def forward_kinematics(q1, q2, q3, q4, q5, q6):
    # Longitudes de los eslabones del robot UR5 en metros
    L1 = 0.089159
    L2 = 0.425
    L3 = 0.39225
    L4 = 0.10915
    L5 = 0.09465
    L6 = 0.0823

    # Matrices de transformación homogénea para cada articulación
    T01 = np.array([
        [math.cos(q1), 0, math.sin(q1), 0],
        [math.sin(q1), 0, -math.cos(q1), 0],
        [0, 1, 0, L1],
        [0, 0, 0, 1]
    ])

    T12 = np.array([
        [math.cos(q2), -math.sin(q2), 0, L2 * math.cos(q2)],
        [math.sin(q2), math.cos(q2), 0, L2 * math.sin(q2)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    T23 = np.array([
        [math.cos(q3), -math.sin(q3), 0, L3 * math.cos(q3)],
        [math.sin(q3), math.cos(q3), 0, L3 * math.sin(q3)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    T34 = np.array([
        [math.cos(q4), 0, math.sin(q4), L4 * math.cos(q4)],
        [math.sin(q4), 0, -math.cos(q4), L4 * math.sin(q4)],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])

    T45 = np.array([
        [math.cos(q5), 0, -math.sin(q5), 0],
        [math.sin(q5), 0, math.cos(q5), 0],
        [0, -1, 0, L5],
        [0, 0, 0, 1]
    ])

    T56 = np.array([
        [math.cos(q6), -math.sin(q6), 0, 0],
        [math.sin(q6), math.cos(q6), 0, 0],
        [0, 0, 1, L6],
        [0, 0, 0, 1]
    ])

    # Matriz de transformación homogénea para la posición final del robot
    T06 = T01.dot(T12).dot(T23).dot(T34).dot(T45).dot(T56)

    return T06
