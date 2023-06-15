# import numpy as np
#
# # Definir la matriz de entrada y el filtro
# matriz_entrada = np.array([[0, 1, 1, 1, 0, 0, 0],
#                            [0, 0, 1, 1, 1, 0, 0],
#                            [0, 0, 0, 1, 1, 1, 0],
#                            [0, 0, 0, 1, 1, 0, 0],
#                            [0, 0, 1, 1, 0, 0, 0],
#                            [0, 1, 1, 0, 0, 0, 0],
#                            [1, 1, 0, 0, 0, 0, 0]])
#
# filtro = np.array([[1, 0, 1],
#                    [0, 1, 0],
#                    [1, 0, 1]])
#
# # Realizar la convolución
# resultado = np.zeros_like(matriz_entrada)  # Matriz de salida con la misma forma que la matriz de entrada
#
# for i in range(1, matriz_entrada.shape[0]-1):
#     for j in range(1, matriz_entrada.shape[1]-1):
#         submatriz = matriz_entrada[i-1:i+2, j-1:j+2]
#         resultado[i, j] = int(np.sum(submatriz*filtro))
#
# # Imprimir la matriz de entrada, el filtro y el resultado
# print("Matriz de entrada:")
# print(matriz_entrada)
#
# print("\nFiltro:")
# print(filtro)
#
# print("\nResultado:")
# print(resultado)


import numpy as np

def convolucion(imagen, kernel):
    alto, ancho = imagen.shape
    kh, kw = kernel.shape
    img_conv = np.zeros((alto - kh + 1, ancho - kw + 1))
    for i in range(alto - kh + 1):
        for j in range(ancho - kw + 1):
            img_conv[i][j] = np.sum(imagen[i:i+kh, j:j+kw] * kernel)
    return img_conv

# Creamos una matriz de características de una imagen
imagen = np.array([[0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 1],
                           [0, 0, 1, 1, 1],
                           [0, 0, 0, 1, 1],
                           [0, 1, 1, 1, 0]
                   ])

# Definimos un kernel
kernel = np.array([[1, 1, 0], [0, 1, 0], [1, 0, 0]])

# Realizamos la convolución
resultado = convolucion(imagen, kernel)

# Imprimimos los resultados
print("Imagen original:\n", imagen)
print("Kernel:\n", kernel)
print("Resultado de la convolución:\n", resultado)