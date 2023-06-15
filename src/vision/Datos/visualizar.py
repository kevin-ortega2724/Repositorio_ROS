import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Carpeta que contiene los archivos binarios
carpeta = '/home/ko/ur_ws/src/vision/Datos/capturas/consolidado/'

# Leer el archivo CSV
df = pd.read_csv('/home/ko/ur_ws/src/vision/Datos/capturas/consolidado1.csv')

# Crear una lista vacía para almacenar las imágenes y las etiquetas
imagenes = []
etiquetas = []

# Iterar sobre las filas del DataFrame
for index, fila in df.iterrows():
    # Obtener el nombre del archivo binario y la etiqueta
    nombre_archivo = fila['imagenes']
    etiqueta_px = fila['px']
    etiqueta_py = fila['py']
    etiqueta_pz = fila['pz']

    # Construir la ruta completa del archivo binario
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        # Leer el archivo binario en una matriz NumPy
        datos = np.fromfile(ruta_archivo, dtype=np.uint8)

        # Obtener las dimensiones de la imagen
        alto, ancho, canales = (480, 640, 12)

        # Convertir los datos en una matriz de imagen
        imagen = datos.reshape((alto, ancho, canales))

        # Agregar la imagen y la etiqueta a las listas correspondientes
        imagenes.append(imagen)
        etiquetas.append([etiqueta_px, etiqueta_py, etiqueta_pz])
    else:
        print(f"El archivo {ruta_archivo} no se encuentra en la ubicación especificada.")

# Convertir las listas en matrices NumPy
imagenes = np.array(imagenes)
etiquetas = np.array(etiquetas)

# Dividir los datos en conjuntos de entrenamiento, validación y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(imagenes, etiquetas, test_size=0.2, random_state=42)
X_entrenamiento, X_validacion, y_entrenamiento, y_validacion = train_test_split(X_entrenamiento, y_entrenamiento, test_size=0.2, random_state=42)

# Imprimir las formas de los conjuntos de datos
print("Forma de X_entrenamiento:", X_entrenamiento.shape)
print("Forma de y_entrenamiento:", y_entrenamiento.shape)
print("Forma de X_validacion:", X_validacion.shape)
print("Forma de y_validacion:", y_validacion.shape)
print("Forma de X_prueba:", X_prueba.shape)
print("Forma de y_prueba:", y_prueba.shape)