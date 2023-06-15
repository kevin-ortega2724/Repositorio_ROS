import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import transforms3d as t3d

# Coordenadas de los primeros 5
points = np.array([[0, 0, 0.089159],
                   [0.343832222609352,	1.52963732158775E-17, 0.338967732224303],
                   [0.42141996081732,	-8.24745794480291E-18,	-0.045532209751989],
                   [0.42141996081732,	-0.10915,	-0.045532209751989],
                   [0.515836054467121,	-0.10915,	-0.052182304481549],
                   [0.521063699777967,	-0.073975178158067,	0.022038269707097]
                   ])

# Matrices de transformación homogéneas
T = []
for i in range(len(points)):
    # Matriz de rotación
    R = t3d.euler.euler2mat(0, 0, 0)
    # Matriz de traslación
    t = points[i]
    T.append(t3d.affines.compose(t, R, [1,1,1]))

# Transformación del extremo del brazo
Te = T[0]
for i in range(1, len(T)):
    Te = np.dot(Te, T[i])

# Representación gráfica
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Puntos de las juntas
ax.scatter(points[:,0], points[:,1], points[:,2], c='black', marker='o')
# Líneas que unen las juntas
for i in range(len(points)-1):
    ax.plot([points[i,0], points[i+1,0]], [points[i,1], points[i+1,1]], [points[i,2], points[i+1,2]], c='gray', linestyle='--')
# Flecha que representa la orientación del extremo del brazo
p0 = Te[:3,3]
v0 = Te[:3,0]
ax.quiver(p0[0], p0[1], p0[2], v0[0], v0[1], v0[2], length=0.1, color='red')
# Cilindro que representa la posición del extremo del brazo
x, y, z = Te[:3,3]
r = 0.03
h = 0.1
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, h, 10)
X = np.outer(np.cos(u), r)
Y = np.outer(np.sin(u), r)
Z = np.outer(np.ones(np.size(u)), v)
X += x
Y += y
Z += z
ax.plot_surface(X, Y, Z, color='blue')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
