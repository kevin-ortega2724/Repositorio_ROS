"""Este script tiene como objetivo generar una representación visual del eje de giro de cada junta
del brazo robótico UR5, utilizando cilindros de diferentes tamaños y posiciones. Esta visualización
puede ayudar a comprender mejor la estructura y movimientos del robot en su entorno de trabajo.

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas de los primeros 5
points = np.array([[0, 0, 0.089159],
                   [0.343832222609352,	1.52963732158775E-17, 0.338967732224303],
                   [0.42141996081732,	-8.24745794480291E-18,	-0.045532209751989],
                   [0.42141996081732,	-0.10915,	-0.045532209751989],
                   [0.515836054467121,	-0.10915,	-0.052182304481549],
                   [0.521063699777967,	-0.073975178158067,	0.022038269707097]
                   ])




# Crea la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Graficar puntos de las juntas
ax.scatter(points[:,0], points[:,1], points[:,2], c='black', marker='o')

# Graficar líneas que unen las juntas
for i in range(len(points)-1):
    ax.plot([points[i,0], points[i+1,0]], [points[i,1], points[i+1,1]], [points[i,2], points[i+1,2]], c='gray', linestyle='--')





ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Mostramos la figura
plt.show()
