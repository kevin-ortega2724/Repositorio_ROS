#!/usr/bin/env python3

"""
Este archivo realiza la operación inversa a la cinemática, obteniendo como entrada los parámetros x, y y z.
Autor @Kevin Ortega
Universidad Tecnológica de Pereira
Ingeniería eléctrica
"""

import rospy
import numpy as np
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

#
# Set the number of samples
num_samples = 10000

# Generate random points in a 3D space
x = np.random.uniform(-1, 1, num_samples)
y = np.random.uniform(-1, 1, num_samples)
z = np.random.uniform(-1, 1, num_samples)

# Calculate the distance of each point from the origin
r = np.sqrt(x**2 + y**2 + z**2)
print(x[0])
# Select only the points that are within the sphere (distance <= 1)
x_in = x[r <= 1]
y_in = y[r <= 1]
z_in = z[r <= 1]

# Plot the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_in, y_in, z_in, c='b', marker='o')

# Set the plot limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
print((x_in[0]))
print(len(y_in))
print(len(z_in))
# Show the plot
plt.show()
#
# Definir la posición objetivo en el espacio
x, y, z = 0.5, 0.3, 0.2

# Función que define la cinemática directa del robot UR5
def forward_kinematics(angles):
    # Matrices de transformación para cada articulación
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
angles = inverse_kinematics([x, y, z])
print(angles)
