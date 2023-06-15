import os
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
# from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
# Cargar el archivo CSV
data = pd.read_csv('capturas/poses.csv', skiprows=1, names=['ruta_imagen1', 'ruta_imagen2','ruta_imagen3', 'theta_i'])

def leer_imagenes(ruta_imagen1, ruta_imagen2, ruta_imagen3):
    img1 = cv2.imread(ruta_imagen1)
    img2 = cv2.imread(ruta_imagen2)
    img3 = cv2.imread(ruta_imagen3)

    if img1 is None or img2 is None or img3 is None:
        print("No se pudo cargar alguna de las imágenes.")
        return None

    if img1.shape[:2] != (480, 640) or img2.shape[:2] != (480, 640) or img3.shape[:2] != (480, 640):
        print("Tamaño de imagen inválido. Se espera (480, 640) pero se encontró", img1.shape[:2], img2.shape[:2], img3.shape[:2])
        return None

    img1 = cv2.resize(img1, (224, 224))
    img2 = cv2.resize(img2, (224, 224))
    img3 = cv2.resize(img3, (224, 224))

    # unir las tres imágenes en un solo tensor
    imagenes = np.concatenate([img1, img2, img3], axis=-1)

    return imagenes


imagenes = []
etiquetas = []

for _, fila in data.iterrows():
    img = leer_imagenes(fila[0], fila[1], fila[2])
    etiqueta = np.array([float(x.strip('[').strip(']')) for x in fila[3].split(',')])
    if img is not None:
        imagenes.append(img)
        etiquetas.append(etiqueta)

imagenes = np.array(imagenes)
etiquetas = np.array(etiquetas)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(imagenes, etiquetas, test_size=0.2)

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 9)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(len(etiquetas[0]))
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Guardar el modelo
model.save('modelo.h5')
