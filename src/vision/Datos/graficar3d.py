import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear las listas de predicciones y valores reales
predicciones = [[0.01587454, 0.00593805, 0.08226164],
                [0.02592455, -0.04724509, 0.49285573],
                [-0.02121974, -0.1726273, 0.27246538],
                [0.04934568, -0.22316572, 0.29732558],
                [-0.14512049, -0.16125591, 0.29455575],
                [-0.01328716, -0.13119784, 0.34971493]]
valores_reales = [[0.0, 0.0, 0.089159],
                  [1.77205176e-17, -4.44245969e-02, 5.11830806e-01],
                  [-5.46909808e-17, -3.61761513e-01, 2.81272040e-01],
                  [-0.10915, -0.36176151, 0.28127204],
                  [-0.10915, -0.36739443, 0.37575428],
                  [-0.04511179, -0.31579082, 0.37883082]]
# # Crear las listas de predicciones y valores reales
# predicciones = [[0.0089891, -0.00665474, 0.07269891],
#                 [0.10464478, 0.11041783, 0.44190085],
#                 [-0.08656354, 0.06759423, 0.7265677],
#                 [-0.16304964, -0.00064549, 0.68276978],
#                 [-0.06594868, 0.02035392, 0.72754645],
#                 [0.0771022, -0.12277557, 0.71497166]]
# valores_reales = [[0.0, 0.0, 0.089159],
#                   [-0.20108739, 0.20108739, 0.40499555],
#                   [0.00503322, -0.00503322, 0.66746203],
#                   [-0.07214748, -0.08221393, 0.66746203],
#                   [-0.07540206, -0.07895935, 0.76200006],
#                   [-0.11586429, -0.00739662, 0.75814347]]


# Convertir las listas en arrays de NumPy
predicciones = np.array(predicciones)
valores_reales = np.array(valores_reales)

# Crear una figura de Matplotlib
fig = plt.figure()

# Crear un subplot 3D
ax = fig.add_subplot(111, projection='3d')

# Dibujar los puntos de las predicciones
for i in range(len(predicciones)):
    ax.scatter(predicciones[i,0], predicciones[i,1], predicciones[i,2], c='r')
    ax.text(predicciones[i,0], predicciones[i,1], predicciones[i,2], f'Joint {i+1}', color='r')

# Dibujar los puntos de los valores reales
for i in range(len(valores_reales)):
    ax.scatter(valores_reales[i,0], valores_reales[i,1], valores_reales[i,2], c='b')
    ax.text(valores_reales[i,0], valores_reales[i,1], valores_reales[i,2], f'Joint {i+1}', color='b')

# Unir los puntos de las predicciones con una línea
ax.plot(predicciones[:,0], predicciones[:,1], predicciones[:,2], c='r', label='Predictions')

# Unir los puntos de los valores reales con una línea
ax.plot(valores_reales[:,0], valores_reales[:,1], valores_reales[:,2], c='b', label='Actual values', alpha=0.5, linestyle='--')

# Agregar leyenda y etiquetas de los ejes
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.set_title('Comparación de predicciones y valores reales')
plt.savefig("grafic3d.svg")
# Mostrar la figura
plt.show()