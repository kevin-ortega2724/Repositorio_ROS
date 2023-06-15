"""
Graficas 3d de los puntos
"""
import numpy as np
import matplotlib.pyplot as plt

valores_reales= np.array([[0.0, 0.0,  0.089159],
                [4.33793953e-16, -1.31332223e-01,  4.93358019e-01],
                [1.59546279e-15, -4.60300753e-01,  2.79723358e-01],
                [0.10915, -0.46030075, 0.27972336],
                [0.10915, -0.54176199, 0.23152907]])

predicciones = np.array([[0.00073329, 0.0012826,  0.1770344],
                        [-0.01367469, -0.16943404,  0.48069862],
                        [0.00598702, -0.41356844,  0.3225849],
                        [0.10006147, -0.3363092,   0.2358484],
                        [0.117112263, -0.47246453,  0.22992133]])

# Crear una figura de Matplotlib
fig = plt.figure()

# Crear un subplot 3D
ax = fig.add_subplot(111, projection='3d')

# Dibujar los puntos de las predicciones
for i in range(len(predicciones)):
    ax.scatter(predicciones[i,0], predicciones[i,1], predicciones[i,2], c='r')
    # ax.text(predicciones[i,0]+0.005, predicciones[i,1]+0.005, predicciones[i,2], f'Joint {i+1}', color='r')
ax.text(predicciones[0,0]+0.005, predicciones[0,1]+0.005, predicciones[0,2], f'Joint {1}', color='r')
ax.text(predicciones[1,0]-0.05, predicciones[1,1]-0.005, predicciones[1,2], f'Joint {2}', color='r')
ax.text(predicciones[2,0]+0.005, predicciones[2,1]+0.005, predicciones[2,2], f'Joint {3}', color='r')
ax.text(predicciones[3,0]+0.005, predicciones[3,1]+0.005, predicciones[3,2], f'Joint {4}', color='r')
ax.text(predicciones[4,0]+0.005, predicciones[4,1]+0.005, predicciones[4,2], f'Joint {5}', color='r')
# ax.text(predicciones[5,0]+0.005, predicciones[5,1]+0.005, predicciones[5,2], f'Joint {i+1}', color='r')


# Dibujar los puntos de los valores reales
for i in range(len(valores_reales)):
    ax.scatter(valores_reales[i,0], valores_reales[i,1], valores_reales[i,2], c='b')
    # ax.text(valores_reales[i,0], valores_reales[i,1]+0.05, valores_reales[i,2]+0.005, f'Joint {i+1}', color='b')

#Coordenadas individuales a puntos

ax.text(valores_reales[0, 0]+0.03, valores_reales[0, 1]-0.07, valores_reales[0,2]+0.05,f'Joint {1}', color='b')
ax.text(valores_reales[1, 0]+0.005, valores_reales[1, 1]+0.005, valores_reales[1,2],f'Joint {2}', color='b')
ax.text(valores_reales[2, 0]-0.07, valores_reales[2, 1]-0.01, valores_reales[2,2]-0.02,f'Joint {3}', color='b')
ax.text(valores_reales[3, 0]-0.05, valores_reales[3, 1]-0.05, valores_reales[3,2],f'Joint {4}', color='b')
ax.text(valores_reales[4, 0]-0.05, valores_reales[4, 1]-0.05, valores_reales[4,2],f'Joint {5}', color='b')
# ax.text(valores_reales[5, 0]-0.05, valores_reales[5, 1]-0.05, valores_reales[5,2],f'Joint {6}', color='b')

# Unir los puntos de las predicciones con una línea
ax.plot(predicciones[:,0], predicciones[:,1], predicciones[:,2], c='r', label='Predictions')

# Unir los puntos de los valores reales con una línea
ax.plot(valores_reales[:,0], valores_reales[:,1], valores_reales[:,2], c='b', label='Actual values', alpha=0.5, linestyle='--')

# Agregar leyenda y etiquetas de los ejes
ax.legend()
plt.xlim(-0.18,0.2)
plt.ylim(-0.5,0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.set_title('Comparación de predicciones y valores reales')
plt.savefig("grafic3d.svg")
# Mostrar la figura
plt.show()