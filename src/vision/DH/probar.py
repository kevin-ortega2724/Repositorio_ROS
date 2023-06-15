from roboticstoolbox import UR5
import numpy as np

# Crear un objeto de robot UR5
robot = UR5()

# Especificar las coordenadas cartesianas deseadas
x, y, z = 0.5, 0.3, 0.2

# Definir una matriz de transformación homogénea para las coordenadas cartesianas
T = np.array([[1, 0, 0, x],
              [0, 1, 0, y],
              [0, 0, 1, z],
              [0, 0, 0, 1]])

# Calcular las coordenadas articulares
q = robot.ikine(T)

# Imprimir las coordenadas articulares
print(q.q)
