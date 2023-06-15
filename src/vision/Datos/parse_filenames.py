"""
Modulo para crear los archivos consolidados
"""

import numpy as np
import pandas
import skimage.io as io

matriz_train = pandas.read_csv('capturas/posestime1d.csv')
# para todas las filas (ejemplos) en la matriz de entrenamiento
for k, fila in matriz_train.iterrows():
    print("fila", k)
    # para cada elemento de la fila
    for i, dato in enumerate(fila):
        # inicializar el stack vacio
        # para i entre 0 y 5 abra el archivo:
        if 0 <= i < 6:
            print(i, dato)
            filedata = io.imread(dato)
            if i == 0:
                stk = filedata
            else:
                stk = np.dstack((stk, filedata))
        # en este punto, stk debe contener todos los canales
        if i >= 6:
            print(stk.shape)
            # save file in ejemplo_k.bin
            stk.tofile('capturas/consolidados2/ejemplo_%04d.bin' % k)
            break

    # if k > 2:  # solo los 4 primeros archivos
    #     break
