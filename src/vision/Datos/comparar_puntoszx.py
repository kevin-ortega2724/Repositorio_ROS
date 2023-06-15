import numpy as np
import matplotlib.pyplot as plt

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

# Proyectar las coordenadas en el plano ZX
predicciones_zx = predicciones[:, [0,2]]
valores_reales_zx = valores_reales[:, [0,2]]

# Crear la figura y los subplots
fig, axs = plt.subplots(ncols=2, figsize=(10,5))

# Graficar las predicciones2 en el primer subplot
axs[0].scatter(predicciones_zx[:, 0], predicciones_zx[:, 1])
axs[0].set_xlabel('X')
axs[0].set_ylabel('Z')
axs[0].set_title('Predicciones')

# Graficar los valores reales en el segundo subplot
axs[1].scatter(valores_reales_zx[:, 0], valores_reales_zx[:, 1])
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')
axs[1].set_title('Valores reales')

# Mostrar la figura
plt.show()
