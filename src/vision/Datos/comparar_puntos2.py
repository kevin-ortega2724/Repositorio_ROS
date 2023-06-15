import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear listas vacías para almacenar los valores de predicción y valor real de cada archivo
predicciones = []
valores_reales = []

# Iterar sobre los nombres de los archivos
for nombre_archivo in ['datos_proceso0.txt', 'datos_proceso1.txt', 'datos_proceso2.txt', 'datos_proceso3.txt', 'datos_proceso4.txt', 'datos_proceso5.txt']:
    # Abrir el archivo
    with open(nombre_archivo, 'r') as f:
        # Leer el contenido del archivo
        contenido = f.read()

        # Buscar los valores de predicción y valor real
        valor_prediccion = [float(x.strip(']')) for x in contenido.split('Predicción: [')[1].split(']')[0].split()]
        valor_real = [float(x.strip(']')) for x in contenido.split('Valor real: [')[1].split(']')[0].split()]

        # Agregar los valores a las listas
        predicciones.append(valor_prediccion)
        valores_reales.append(valor_real)

# Convertir las listas en arrays numpy
predicciones = np.array(predicciones)
valores_reales = np.array(valores_reales)

# Crear la figura y los subplots
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Graficar las predicciones2 en el primer subplot
ax1.scatter(predicciones[:, 0], predicciones[:, 1], predicciones[:, 2])
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Predicciones')

# Graficar los valores reales en el segundo subplot
ax2.scatter(valores_reales[:, 0], valores_reales[:, 1], valores_reales[:, 2])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Valores reales')

# Convertir las listas en arrays de NumPy
predicciones = np.array(predicciones)
valores_reales = np.array(valores_reales)

# Crear una figura de Matplotlib
fig = plt.figure()

# Crear un subplot 3D
ax = fig.add_subplot(111, projection='3d')

# Dibujar los puntos de las predicciones2
ax.scatter(predicciones[:,0], predicciones[:,1], predicciones[:,2], c='r', label='Predicciones')

# Dibujar los puntos de los valores reales
ax.scatter(valores_reales[:,0], valores_reales[:,1], valores_reales[:,2], c='b', label='Valores reales')

# Unir los puntos de las predicciones2 con una línea
ax.plot(predicciones[:,0], predicciones[:,1], predicciones[:,2], c='r', label='Predicciones')

# Unir los puntos de los valores reales con una línea
ax.plot(valores_reales[:,0], valores_reales[:,1],valores_reales[:,2], c='b', label='Valores reales', alpha=0.5, linestyle='--')

ax.plot(predicciones[:,0], predicciones[:,1],
predicciones[:,2], c='r', alpha=0.5, linestyle='--')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Comparación de predicciones2 y valores reales')

plt.show()