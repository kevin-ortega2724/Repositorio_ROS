# import pandas as pd
# from skimage import io
#
# def process_data(img1, img2, img3, theta_i):
#     # Imprimir dimensiones de las imágenes y el vector theta_i
#     print(f"Dimensiones img1: {img1.shape}")
#     print(f"Dimensiones img2: {img2.shape}")
#     print(f"Dimensiones img3: {img3.shape}")
#     print(f"Vector theta_i: {theta_i}")
# # Leer el archivo CSV
# data = pd.read_csv('capturas/poses.csv')
#
# # Recorrer cada fila del CSV
# for index, row in data.iterrows():
#     # Leer las imágenes usando las rutas de columna
#     img1 = io.imread(row['ruta_imagen1'])
#     img2 = io.imread(row['ruta_imagen2'])
#     img3 = io.imread(row['ruta_imagen3'])
#     # print(img3)
#     # Extraer el vector theta_i
#     theta_i = [float(val) for val in row['theta_i'][1:-1].split(',')]
#     # print(len(theta_i))
#     # Procesar datos
#     process_data(img1, img2, img3, theta_i)
import matplotlib.pyplot as plt
# imagen = cv2.imread("/home/ko/ur_ws/src/vision/Datos/capturas/raw/img_[0.0, -2.5132741228718345, -2.0, 175.2974883876273, 11.584004844603628, 7.64143905720585].png")
#
#
# # Convertir de BGR a RGB
# imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
#
# # Mostrar imagen
# plt.imshow(imagen)
# plt.show()
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0" # Reemplaza "0" con el índice de la GPU que deseas utilizar
