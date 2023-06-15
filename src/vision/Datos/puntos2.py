# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Definimos las dos posiciones
# pos1 = np.array([1, 2, 3])
# pos2 = np.array([4, 5, 6])
#
# # Creamos los datos para el cilindro
# z = np.linspace(-1, 1, 100)
# theta = np.linspace(0, 2*np.pi, 100)
# theta_grid, z_grid = np.meshgrid(theta, z)
#
# # Creamos la figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Dibujamos los cilindros en cada posición
# for pos in [pos1, pos2]:
#     # Obtenemos el vector normalizado de la posición
#     vec_norm = pos / np.linalg.norm(pos)
#
#     # Calculamos el vector perpendicular
#     vec_perp = np.array([vec_norm[1], -vec_norm[0], 0])
#
#     # Normalizamos el vector perpendicular
#     vec_perp_norm = vec_perp / np.linalg.norm(vec_perp)
#
#     # Calculamos el punto central del cilindro
#     center = pos - vec_norm * np.linalg.norm(pos) / 2
#
#     # Dibujamos el cilindro
#     ax.plot_surface(
#         center[0] + vec_perp_norm[0] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[1] + vec_perp_norm[1] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[2] + vec_perp_norm[2] * np.outer(np.cos(theta), np.ones_like(z)) + np.outer(np.sin(theta), z),
#         alpha=0.5,
#         color='b'
#     )
#
# # Configuramos los ejes y mostramos la figura
# ax.set_xlim(-6, 6)
# ax.set_ylim(-6, 6)
# ax.set_zlim(-6, 6)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()
#------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos las posiciones
pos = np.array([[0, 0, 0.089159],
                       [0.343832222609351, 1.52963732158776E-17, -0.160649732224304],
                       [0.421419960817322, -8.2474579448028E-18, 0.223850209751987],
                       [0.421419960817322, 0.10915, 0.223850209751987],
                       [0.184171092920166, 0.704961115177957, -0.345506869046183],
                       ])
# pos_norm = pos1 / np.linalg.norm(pos1)
# Creamos los datos para el cilindro
z = np.linspace(-0.2, 0.2, 100)
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, z_grid = np.meshgrid(theta, z)
x_grid = np.cos(theta_grid)
y_grid = np.sin(theta_grid)

# Creamos la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Graficar puntos de las juntas
ax.scatter(pos[:,0], pos[:,1], pos[:,2], c='black', marker='o')

# Dibujamos los cilindros en cada posición
for pos in [pos[0], pos[1], pos[2], pos[3], pos[4]]:
    # Normalizamos el vector de posición
    pos_norm = pos / np.linalg.norm(pos)

    # Calculamos el vector perpendicular al vector de posición con la dirección deseada
    vec_perp1 = np.cross(pos_norm, np.array([0, 0, 1]))
    vec_perp2 = np.cross(vec_perp1, np.array([1, 0, 0]))
    vec_perp_norm = vec_perp2 / np.linalg.norm(vec_perp2)

    # Calculamos el punto central del cilindro

    center1 = pos_norm

    # Dibujamos el cilindro
    ax.plot_surface(
        center1[0] + x_grid * 0.2,
        center1[1] + y_grid * 0.2,
        center1[2] + z_grid * 0.2,
        alpha=0.5,
        color='b'
    )



# Configuramos los ejes y mostramos la figura
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
#-----------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Definimos las posiciones
# pos = np.array([
#     [0, 0, 0.089159],
#     [0.343832222609351, 1.52963732158776E-17, -0.160649732224304],
#     [0.421419960817322, -8.2474579448028E-18, 0.223850209751987],
#     [0.421419960817322, 0.10915, 0.223850209751987],
#     [0.184171092920166, 0.704961115177957, -0.345506869046183]
# ])
#
# # Creamos la figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Dibujamos los cilindros en cada posición
# for p in [pos[0],pos[1], pos[2], pos[3], pos[4]]:
#     # Normalizamos el vector de posición
#     pos_norm = p / np.linalg.norm(p)
#
#     # Calculamos el vector perpendicular al vector de posición
#     vec_perp = np.cross(pos_norm, np.array([0, 0, 1]))
#     vec_perp_norm = vec_perp / np.linalg.norm(vec_perp)
#
#     # Calculamos el punto central del cilindro
#     center1 = p
#     center2 = p + vec_perp_norm * 0.2
#
#     # Creamos los datos para el cilindro
#     z = np.linspace(-0.2, 0.2, 100)
#     theta = np.linspace(0, 2*np.pi, 100)
#     theta_grid, z_grid = np.meshgrid(theta, z)
#     x_grid = np.cos(theta_grid) * 0.01 + center1[0]
#     y_grid = np.sin(theta_grid) * 0.01 + center1[1]
#
#     # Dibujamos el cilindro
#     ax.plot_wireframe(
#         x_grid,
#         y_grid,
#         z_grid + center2[2],
#         alpha=0.5,
#         color='b'
#     )
#
# # Configuramos los ejes y mostramos la figura
# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)
# ax.set_zlim(-1, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Definimos las dos posiciones
# pos1 = np.array([0, 0, 0.089159])
# pos2 = np.array([0.343832222609351, 1.52963732158776E-17, -0.160649732224304])
#
# # Vector de dirección de los cilindros
# dir_vec = np.array([1, 1, 0])
#
# # Creamos los datos para el cilindro
# z = np.linspace(-1, 1, 500)
# theta = np.linspace(0, 2*np.pi, 500)
# theta_grid, z_grid = np.meshgrid(theta, z)
#
# # Creamos la figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Dibujamos los cilindros en cada posición
# for pos in [pos1, pos2]:
#     # Calculamos el vector perpendicular al vector de dirección
#     vec_perp = np.cross(dir_vec, pos)
#     vec_perp_norm = vec_perp / np.linalg.norm(vec_perp)
#
#     # Calculamos el punto central del cilindro
#     center = pos - dir_vec * np.linalg.norm(pos) / 2
#
#     # Dibujamos el cilindro
#     ax.plot_surface(
#         center[0] + vec_perp_norm[0] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[1] + vec_perp_norm[1] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[2] + vec_perp_norm[2] * np.outer(np.cos(theta)*0.1, np.ones_like(z))*0.1 + np.outer(np.sin(theta), z)*0.5,
#         alpha=0.5,
#         color='b'
#     )
#
# # Configuramos los ejes y mostramos la figura
# ax.set_box_aspect([1,1,1])
# # ax.set_xlim(-1, 1)
# # ax.set_ylim(-1, 1)
# # ax.set_zlim(-1, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.view_init(azim=45)
# plt.show()


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
#
# # Definir posiciones de las juntas
# joints = np.array([[0, 0, 0.089159],
#                        [0.343832222609351, 1.52963732158776E-17, -0.160649732224304],
#                        [0.421419960817322, -8.2474579448028E-18, 0.223850209751987],
#                        [0.421419960817322, 0.10915, 0.223850209751987],
#                        [0.184171092920166, 0.704961115177957, -0.345506869046183],
#                        ])
#
# # Crear figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Graficar puntos de las juntas
# ax.scatter(joints[:,0], joints[:,1], joints[:,2], c='b', marker='o')
#
# # Graficar líneas que unen las juntas
# for i in range(len(joints)-1):
#     ax.plot([joints[i,0], joints[i+1,0]], [joints[i,1], joints[i+1,1]], [joints[i,2], joints[i+1,2]], c='r')
#
# # Configurar límites de los ejes
# ax.set_xlim([-0.9, 0.9])
# ax.set_ylim([-0.9, 0.9])
# ax.set_zlim([-0.9, 0.9])
#
# # Etiquetar ejes
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # Mostrar figura
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# Definimos las posiciones de las juntas
# positions = np.array([
#     [0, 0, 0],
#     [0, 0, 0.5],
#     [0, 0.5, 0.5],
#     [0.5, 0.5, 0.5],
#     [0.5, 0.5, 0]
# ])
#
# # Vector de dirección de los cilindros
# dir_vec = np.array([1, 1, 0])
#
# # Definimos la resolución de los cilindros
# theta_res = 50
# z_res = 50
#
# # Creamos la figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Dibujamos los cilindros en cada posición
# for pos in positions:
#     # Calculamos el vector perpendicular al vector de dirección
#     vec_perp = np.cross(dir_vec, pos)
#     vec_perp_norm = vec_perp / np.linalg.norm(vec_perp)
#
#     # Calculamos el punto central del cilindro
#     center = pos - dir_vec * np.linalg.norm(pos) / 2
#
#     # Creamos los datos para el cilindro
#     z = np.linspace(-1, 1, z_res)
#     theta = np.linspace(0, 2*np.pi, theta_res)
#     theta_grid, z_grid = np.meshgrid(theta, z)
#
#     # Dibujamos el cilindro
#     ax.plot_surface(
#         center[0] + vec_perp_norm[0] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[1] + vec_perp_norm[1] * np.outer(np.cos(theta), np.ones_like(z)),
#         center[2] + vec_perp_norm[2] * np.outer(np.cos(theta), np.ones_like(z)) + np.outer(np.sin(theta), z),
#         alpha=0.5,
#         color='b'
#     )
#
# # Configuramos los ejes y mostramos la figura
# ax.set_box_aspect([1,1,1])
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generamos un vector aleatorio
# vec = np.random.rand(3)
# vec_norm = vec / np.linalg.norm(vec)
#
# # Generamos una posición aleatoria
# pos = np.random.rand(3)
#
# # Creamos los datos para el cilindro
# z = np.linspace(-0.5, 0.5, 100)
# theta = np.linspace(0, 2*np.pi, 100)
# theta_grid, z_grid = np.meshgrid(theta, z)
#
# # Calculamos el vector perpendicular al vector de dirección
# vec_perp = np.cross(vec_norm, pos)
# vec_perp_norm = vec_perp / np.linalg.norm(vec_perp)
#
# # Calculamos el punto central del cilindro
# center = pos - vec_norm / 2
#
# # Creamos la figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Dibujamos el cilindro
# ax.plot_surface(
#     center[0] + vec_perp_norm[0] * 0.1 * np.outer(np.cos(theta), np.ones_like(z)),
#     center[1] + vec_perp_norm[1] * 0.1 * np.outer(np.cos(theta), np.ones_like(z)),
#     center[2] + vec_perp_norm[2] * 0.1 * np.outer(np.cos(theta), np.ones_like(z)) + np.outer(np.sin(theta), z),
#     alpha=0.5,
#     color='b'
# )
#
# # Dibujamos el punto
# ax.scatter(pos[0], pos[1], pos[2], s=50, color='r')
#
# # Configuramos los ejes y mostramos la figura
# ax.set_box_aspect([1,1,1])
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Generamos los datos del cilindro
# r = 1
# h = 2
# t = np.linspace(0, 2*np.pi, 100)
# z = np.linspace(0, h, 10)
# T, Z = np.meshgrid(t, z)
# X = r * np.cos(T)
# Y = r * np.sin(T)
#
# # Creamos la figura y los ejes
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # Graficamos el cilindro
# ax.plot_surface(X, Y, Z, alpha=0.5)
#
# # Configuramos los ejes
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # Mostramos la gráfica
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from sympy import symbols, cos, sin, simplify
# from sympy import *
# from sympy import *
# from sympy.abc import theta1, theta2
#
# theta1 = float(theta1)
# theta2 = float(theta2)
#
# # Definimos los símbolos y las constantes
# theta1, theta2, L1, L2 = symbols('theta1 theta2 L1 L2')
#
# # Definimos la cinemática directa del manipulador
# x = L1*cos(theta1) + L2*cos(theta1 + theta2)
# y = L1*sin(theta1) + L2*sin(theta1 + theta2)
#
# # Simplificamos la expresión
# x = simplify(x)
# y = simplify(y)
#
# # Convertimos las constantes a números de punto flotante
# L1 = 1.0
# L2 = 1.0
#
# # Creamos la figura y los ejes
# fig, ax = plt.subplots()
#
# # Graficamos los eslabones
# ax.plot([0, L1*cos(theta1)], [0, L1*sin(theta1)], 'b-', lw=2)
# ax.plot([L1*cos(theta1), x], [L1*sin(theta1), y], 'r-', lw=2)
#
# # Graficamos las articulaciones
# ax.plot(0, 0, 'ko', ms=8)
# ax.plot(L1*cos(theta1), L1*sin(theta1), 'ko', ms=8)
#
# # Configuramos los ejes
# ax.set_xlim(-1.5*(L1 + L2), 1.5*(L1 + L2))
# ax.set_ylim(-1.5*(L1 + L2), 1.5*(L1 + L2))
# ax.set_aspect('equal', adjustable='box')
# ax.grid(True)
#
# # Mostramos la gráfica
# plt.show()
#
