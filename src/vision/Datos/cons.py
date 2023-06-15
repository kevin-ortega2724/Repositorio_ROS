import numpy as np
import math
import csv
from scipy.spatial.transform import Rotation as R
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

filename = 'capturas/poses.csv'

positions = []
orientations = []

# Abrir el archivo CSV
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # omitir la primera fila
    poses = []
    for row in reader:
        q1, q2, q3, q4, q5, q6 = list(map(float, row[3].strip('[]').split(', ')))
        # usar la cinemática directa para obtener los parámetros

        # Convertir las coordenadas angulares a radianes si no lo están ya
        q1 = math.radians(q1)
        q2 = math.radians(q2)
        q3 = math.radians(q3)
        q4 = math.radians(q4)
        q5 = math.radians(q5)
        q6 = math.radians(q6)

        # Definir la matriz de transformación homogénea de la base al efector final
        T = forward_kinematics(q1, q2, q3, q4, q5, q6)

        # Extraer los parámetros de posición y orientación de la matriz de transformación homogénea
        position = T[:3, 3]
        orientation = R.from_matrix(T[:3, :3]).as_quat()

        # agregar la posición y orientación a las listas correspondientes
        positions.append(position)
        orientations.append(orientation)

        # Imprimir los parámetros de posición y orientación
        print(f"Posición: {position}")
        print(f"Orientación: {orientation}")

# combinar las listas de posición y orientación en una sola lista para guardarlas en un archivo CSV
poses = []
for i in range(len(positions)):
    pose = list(positions[i]) + list(orientations[i])
    poses.append(pose)

# guardar la lista de poses en un archivo CSV
with open('poseszzz.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(poses)