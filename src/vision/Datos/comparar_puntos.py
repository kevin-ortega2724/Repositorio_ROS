import numpy as np
import re
import matplotlib.pyplot as plt

# Crear listas vacías para almacenar las predicciones2 y valores reales
predicciones_procesos = []
valores_reales_procesos = []

# Leer los datos de los archivos y almacenarlos en las listas correspondientes
for proceso in range(5):
    nombre_archivo = f"datos_proceso{proceso + 1}.txt"
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.readlines()
    predicciones_proceso = []
    valores_reales_proceso = []
    for linea in datos:
        valores = linea.split(",")
        if len(valores) != 6:
            continue
        pattern = r'[-+]?\d*\.\d+|\d+'
        numbers = re.findall(pattern, "".join(valores))
        pred = [float(numbers[i]) for i in range(3)]
        real = [float(numbers[i]) for i in range(3, 6)]
        predicciones_proceso.append(pred)
        valores_reales_proceso.append(real)
    predicciones_procesos.append(predicciones_proceso)
    valores_reales_procesos.append(valores_reales_proceso)

# Convertir las listas a arrays de numpy
predicciones_procesos = np.array(predicciones_procesos)
valores_reales_procesos = np.array(valores_reales_procesos)

# Comparar las i iteraciones de cada proceso y encontrar la más parecida
num_procesos = predicciones_procesos.shape[0]
num_iteraciones = predicciones_procesos.shape[1]
num_variables = predicciones_procesos.shape[2] if len(predicciones_procesos.shape) > 2 else 1

indices_mas_parecidos = []
for i in range(num_iteraciones):
    # Crear un array con las i-ésimas predicciones2 y valores reales de cada proceso
    pred_i = predicciones_procesos[:, i, :]
    real_i = valores_reales_procesos[:, i, :]

    # Calcular la distancia euclidiana entre las predicciones2 y valores reales de cada proceso
    distancias = np.linalg.norm(pred_i - real_i, axis=1)

    # Encontrar el índice del proceso con la distancia más pequeña
    indice_mas_parecido = np.argmin(distancias)

    # Almacenar el índice del proceso más parecido a la i-ésima iteración
    indices_mas_parecidos.append(indice_mas_parecido)

    # Graficar los puntos más parecidos si hay más de un índice
    indices_iteracion_i = np.where(np.array(indices_mas_parecidos) == i)[0]
    if len(indices_iteracion_i) > 1:
        print(f"En la iteración {i} hay {len(indices_iteracion_i)} índices:")
        print(indices_iteracion_i)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        for indice_proceso in indices_iteracion_i:
            pred_i = predicciones_procesos[indice_proceso, i, :]
            ax.scatter(pred_i[0], pred_i[1], pred_i[2])
            ax.set_title(f'Iteración {i}')
            plt.show()

    # if len(indices_iteracion_i) > 1:
    #     print(f"En la iteración {i} hay {len(indices_iteracion_i)} índices:")
    #     print(indices_iteracion_i)
    #     fig = plt.figure()
    #     ax = fig.add_subplot(projection='3d')
    #     for indice_proceso in indices_iteracion_i:
    #
