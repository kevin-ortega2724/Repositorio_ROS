import numpy as np

# Parámetros DH del robot UR5
d1, a2, a3, d4, d5, d6 = 0.089159, -0.425, -0.39225, 0.10915, 0.09465, 0.0823

# Matriz de transformación homogénea T del robot UR5 en su posición de reposo
T = np.array([[ 1, 0,  0,         0],
              [ 0, 1,  0,         0],
              [ 0, 0,  1,  0.089159],
              [ 0, 0,  0,         1]])

# Transformación de la base al eslabón 1
T = T @ np.array([[ np.cos(np.pi/2), -np.sin(np.pi/2), 0, 0],
                  [ np.sin(np.pi/2),  np.cos(np.pi/2), 0, 0],
                  [               0,               0, 1, 0],
                  [               0,               0, 0, 1]])

# Transformación del eslabón 1 al eslabón 2
T = T @ np.array([[ np.cos(np.pi), 0,  np.sin(np.pi),        0],
                  [ np.sin(np.pi), 0, -np.cos(np.pi),        0],
                  [            0, 1,             0, -0.42500],
                  [            0, 0,             0,        1]])

# Transformación del eslabón 2 al eslabón 3
T = T @ np.array([[ np.cos(np.pi), 0,  np.sin(np.pi),        0],
                  [ np.sin(np.pi), 0, -np.cos(np.pi),        0],
                  [            0, 1,             0, -0.39225],
                  [            0, 0,             0,        1]])

# Transformación del eslabón 3 al eslabón 4
T = T @ np.array([[ np.cos(-np.pi/2), -np.sin(-np.pi/2), 0, -0.10915],
                  [ np.sin(-np.pi/2),  np.cos(-np.pi/2), 0,       0],
                  [                0,                0, 1, -0.39225],
                  [                0,                0, 0,       1]])

# Transformación del eslabón 4 al eslabón 5
T = T @ np.array([[ np.cos(np.pi), 0,  np.sin(np.pi),        0],
                  [ np.sin(np.pi), 0, -np.cos(np.pi),        0],
                  [            0, 1,             0, 0.09465],
                  [            0, 0,             0,        1]])

T = T @ np.array([[ np.cos(-np.pi/2), -np.sin(-np.pi/2), 0,        0],
                  [ np.sin(-np.pi/2),  np.cos(-np.pi/2), 0,        0],
                  [                0,                0, 1,  0.19145],
                  [                0,                0, 0,        1]])

# Transformación del sistema de coordenadas del eslabón 5 al eslabón 6
# Matriz de transformación homogénea final
T = T @ np.array([[ 1, 0,  0, 0],
                  [ 0, 1,  0, 0],
                  [ 0, 0,  1, d6],
                  [ 0, 0,  0, 1]])

# Imprimir la matriz de transformación homogénea final
print(T)


