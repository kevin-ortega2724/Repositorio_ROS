import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Punto que queremos graficar el cilindro alrededor
# x0, y0, z0 = 0, 0, 0.089
# radius = 0.001
# height = 0.11
#
# # Generar las coordenadas x e y
# u = np.linspace(0, 2*np.pi, 30)
# v = np.linspace(0, height, 30)
# u, v = np.meshgrid(u, v)
# x = x0 + radius * np.cos(u)
# y = y0 + radius * np.sin(u)
# z = z0 + v
#
# # Crea la figura y el eje tridimensional
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# #
# # # Grafica el cilindro
# # ax.plot_surface(x, y, z, alpha=0.5)
#
# # Grafica el punto
# ax.scatter(x0, y0, z0, color='r')
#
# # Muestra el gráfico
# plt.show()


# # Definir las posiciones de los enlaces del robot
# posiciones = np.array([[0, 0, 0.089159],
#                        [0.343832222609351, 1.52963732158776E-17, -0.160649732224304],
#                        [0.421419960817322, -8.2474579448028E-18, 0.223850209751987],
#                        [0.421419960817322, 0.10915, 0.223850209751987],
#                        [0.184171092920166, 0.704961115177957, -0.345506869046183],
#                        [0.284171092920166, 0.7604961115177957, -0.445506869046183]])
#
# # Crear una figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Graficar los puntos de posición de los enlaces
# ax.scatter(posiciones[:, 0], posiciones[:, 1], posiciones[:, 2], color='black', s=10)
#
# # Graficar los cilindros
# for i in range(len(posiciones)-1):
#     # Encontrar la dirección perpendicular al vector incidente
#     v1 = posiciones[i + 1] - posiciones[i]
#     if i > 0:
#         v2 = posiciones[i] - posiciones[i - 1]
#         v1 = v1 / np.linalg.norm(v1) - v2 / np.linalg.norm(v2)
#     perpendicular = np.cross(v1, [0, 0, 1])
#     perpendicular /= np.linalg.norm(perpendicular)
#
#     # Definir el radio y la altura del cilindro
#     radio = 0.05
#     altura = np.linalg.norm(v1)
#
#     # Definir la posición del centro del cilindro
#     p = posiciones[i]
#
#     # Generar las coordenadas para la superficie del cilindro
#     z = np.linspace(p[2], p[2] + altura, 20)
#     theta = np.linspace(0, 2 * np.pi, 30)
#     theta, z = np.meshgrid(theta, z)
#     x = p[0] + radio * np.cos(theta) * perpendicular[0]
#     y = p[1] + radio * np.sin(theta) * perpendicular[1]
#
#     # Graficar la superficie del cilindro
#     ax.plot_surface(x, y, z, color='blue', alpha=0.5)
#
# plt.show()
# print(len(posiciones))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from spatialmath import base


def cylinder(p0, v, radius, ax, color='r', alpha=1.0, label=None):
    # Generar el vector perpendicular al vector incidente
    not_v = np.array([1, 0, 0])
    if (not_v == v).all():
        not_v = np.array([0, 1, 0])
    n1 = np.cross(v, not_v)
    n1 /= np.linalg.norm(n1)

    # Generar otro vector perpendicular a ambos
    n2 = np.cross(v, n1)
    n2 /= np.linalg.norm(n2)

    # Generar puntos de la circunferencia
    theta = np.linspace(0, 2 * np.pi, 50)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Generar puntos del cilindro
    C = np.zeros((len(x), 3))
    for i in range(len(x)):
        C[i] = p0 + x[i] * n1 + y[i] * n2

    # Ajustar tamaño del cilindro
    # z = np.linspace(0, np.linalg.norm(v), 50)
    R = np.array([v, n1, n2]).T
    C = np.dot(C - p0, R) + p0

    # Dibujar cilindro
    ax.plot(C[:, 0], C[:, 1], C[:, 2], color=color, alpha=alpha, label=label)

    return ax


# Definir las posiciones de los enlaces del robot
posiciones = np.array([[0, 0, 0.089159],
                       [0.343832222609351, 1.52963732158776E-17, -0.160649732224304],
                       [0.421419960817322, -8.2474579448028E-18, 0.223850209751987],
                       [0.421419960817322, 0.10915, 0.223850209751987],
                       [0.184171092920166, 0.704961115177957, -0.345506869046183]])

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar los puntos de posición de los enlaces
ax.scatter(posiciones[:,0], posiciones[:,1], posiciones[:,2], color='black', s=10)

# Dibujar los cilindros
radius = 0.01
for i in range(len(posiciones)-1):
    v1 = posiciones[i + 1] - posiciones[i]
    cylinder(posiciones[-4], v1, radius, ax, color='red', alpha=1, label='Cilindro 5')
    cylinder(posiciones[-1], v1, radius, ax, color='red', alpha=1, label='Cilindro 5')
    cylinder(posiciones[-3], v1, radius, ax, color='red', alpha=0.5, label='Cilindro 5')
    cylinder(posiciones[-2], v1, radius, ax, color='green', alpha=0.5, label='Cilindro 5')
    cylinder(posiciones[-5], v1, radius, ax, color='blue', alpha=1, label='Cilindro 5')
    # cylinder(posiciones[0], v1, radius, ax, color='blue', alpha=0.5, label='Cilindro 5')


# Dibujar el último cilindro
# v1 = posiciones[-1] - posiciones[-2]
# cylinder(posiciones[-1], v1, radius, ax, color='blue', alpha=0.5)

plt.show()
