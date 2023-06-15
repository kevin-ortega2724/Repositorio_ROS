import csv
import numpy as np
from scipy.spatial.transform import Rotation as R

# Longitudes de los eslabones del robot UR5 en metros
L1 = 0.089159
L2 = 0.425
L3 = 0.39225
L4 = 0.10915
L5 = 0.09465
L6 = 0.0823

def forward_kinematics(q1, q2, q3, q4, q5, q6):
    # Matrices de transformación homogénea para cada articulación
    T01 = np.array([
        [np.cos(q1), 0, np.sin(q1), 0],
        [np.sin(q1), 0, -np.cos(q1), 0],
        [0, 1, 0, L1],
        [0, 0, 0, 1]
    ])

    T12 = np.array([
        [np.cos(q2), -np.sin(q2), 0, L2 * np.cos(q2)],
        [np.sin(q2), np.cos(q2), 0, L2 * np.sin(q2)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    T23 = np.array([
        [np.cos(q3), -np.sin(q3), 0, L3 * np.cos(q3)],
        [np.sin(q3), np.cos(q3), 0, L3 * np.sin(q3)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    T34 = np.array([
        [np.cos(q4), 0, np.sin(q4), L4 * np.cos(q4)],
        [np.sin(q4), 0, -np.cos(q4), L4 * np.sin(q4)],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])

    T45 = np.array([
        [np.cos(q5), 0, -np.sin(q5), 0],
        [np.sin(q5), 0, np.cos(q5), 0],
        [0, -1, 0, L5],
        [0, 0, 0, 1]
    ])

    T56 = np.array([
        [np.cos(q6), -np.sin(q6), 0, 0],
        [np.sin(q6), np.cos(q6), 0, 0],
        [0, 0, 1, L6],
        [0, 0, 0, 1]
    ])

    # Matriz de transformación homogénea para la posición final del robot
    T06 = T01.dot(T12).dot(T23).dot(T34).dot(T45).dot(T56)

    # Extraer los parámetros de posición y orientación de la matriz de transformación homogénea
    position = T06[:3, 3]
    orientation = R.from_matrix(T06[:3, :3]).as_quat()

    return position, orientation

filename = 'poseszzz.csv'

# Abrir el archivo CSV
with open(filename, 'r') as f:

    reader = csv.reader(f)

    next(reader)  # omitir la primera fila
    for row in reader:

        # Convertir las coordenadas angulares a radianes si no lo están ya
        q1, q2, q3, q4, q5, q6 = list(map(float, row[0:]))


        # Calcular la posición y orientación correspondiente
        position, orientation = forward_kinematics(q1, q2, q3, q4, q5, q6)

        # Imprimir los resultados
        print(f"Coordenadas articulares: {q1}, {q2}, {q3}, {q4}, {q5}, {q6}")
        print(f"Posición: {position}")
        print(f"Orientación: {orientation}")
        print(len(position))
        print(row)

