import csv

import fk as fk
import numpy as np
import math
from fk import forward_kinematics
from scipy.spatial.transform import Rotation as R
import tf3d



# Función para calcular la matriz de transformación homogénea DH
# def DHMatrix(a, alpha, d, theta):
#     cosTheta = math.cos(theta)
#     sinTheta = math.sin(theta)
#     cosAlpha = math.cos(alpha)
#     sinAlpha = math.sin(alpha)
#     return np.array([
#         [cosTheta, -sinTheta * cosAlpha, sinTheta * sinAlpha, a * cosTheta],
#         [sinTheta, cosTheta * cosAlpha, -cosTheta * sinAlpha, a * sinTheta],
#         [0, sinAlpha, cosAlpha, d],
#         [0, 0, 0, 1]
#     ])
#
#
# # Función para calcular los parámetros DH
# def DHParams(thetas):
#     # Longitudes de los eslabones del robot UR5 en metros
#     a = [0, -0.425, -0.39225, 0, 0, 0]
#     # Desplazamientos de los eslabones del robot UR5 en metros
#     d = [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
#     # Ángulos de rotación en radianes
#     alpha = [math.pi / 2, 0, 0, math.pi / 2, -math.pi / 2, 0]
#     # Ángulos de rotación en radianes
#     theta = thetas
#
#     # Calcular las matrices de transformación homogénea para cada eslabón
#     T01 = DHMatrix(a[0], alpha[0], d[0], theta[0])
#     T12 = DHMatrix(a[1], alpha[1], d[1], theta[1])
#     T23 = DHMatrix(a[2], alpha[2], d[2], theta[2])
#     T34 = DHMatrix(a[3], alpha[3], d[3], theta[3])
#     T45 = DHMatrix(a[4], alpha[4], d[4], theta[4])
#     T56 = DHMatrix(a[5], alpha[5], d[5], theta[5])
#
#     # Calcular la matriz de transformación homogénea para el punto final del robot UR5
#     T06 = T01.dot(T12).dot(T23).dot(T34).dot(T45).dot(T56)
#
#     # Extraer los parámetros a partir de la matriz de transformación homogénea
#     x = T06[0][3]
#     y = T06[1][3]
#     z = T06[2][3]
#     Rx = math.atan2(T06[2][1], T06[2][2])
#     Ry = math.atan2(-T06[2][0], math.sqrt(T06[2][1] ** 2 + T06[2][2] ** 2))
#     Rz = math.atan2(T06[1][0], T06[0][0])
#
#     # Convertir los ángulos a grados
#     Rx = math.degrees(Rx)
#     Ry = math.degrees(Ry)
#     Rz = math.degrees(Rz)
#
#     return [x, y, z, Rx, Ry, Rz]



# Ruta del archivo CSV
filename = 'capturas/poses.csv'

positions = []
orientations = []
# Abrir el archivo CSV
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # omitir la primera fila
    poses = [] #No olvidar pasarlos a un scv
    positions = []
    orientations = []
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
        T = fk.forward_kinematics(q1, q2, q3, q4, q5, q6)

        # Extraer los parámetros de posición y orientación de la matriz de transformación homogénea
        position = T[:3, 3]
        orientation = R.from_matrix(T[:3, :3]).as_quat()
        # agregar la posición y orientación a las listas correspondientes
        positions.append(position)
        orientations.append(orientation)

        # Imprimir los parámetros de posición y orientación
        print(f"Posición: {position}")
        print(f"Orientación: {orientation}")
        # pose = np.concatenate([position, orientation])
        # poses.append(pose)
        # combinar las listas de posición y orientación en una sola lista para guardarlas en un archivo CSV
    for i in range(len(positions)):
        pose = list(positions[i]) + list(orientations[i])
        poses.append(pose)

    # guardar la lista de poses en un archivo CSV
    with open('posesxyzborrar.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(poses)   #3estas lineas comentadas guardan el archivo, recordar que lo hiciste a pedal, con las mismas rutas

        # Ruta del archivo CSV para guardar las poses


# convertir la lista de poses en un array de numpy
poses = np.array(poses)


# guardar los vectores de posición y orientación en columnas separadas
np.savetxt("posesxyzc.csv", poses, delimiter=",")
