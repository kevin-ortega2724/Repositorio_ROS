import csv
import numpy as np
# Lista de predicciones
predicciones = [[0.01587454, 0.00593805, 0.08226164],
                [ 0.0089891,  -0.00665474,  0.07269891],
                [ 0.01797587, -0.0049786,   0.10525992],
                [-0.00404299, - 0.01190037, 0.0870373],
                [ 0.00952778, -0.01541634,  0.09874065],
                [-0.00837072,  0.01575068 , 0.09161692],
                [-0.00414863, -0.04824197,  0.10742213],
                [-0.00523161, -0.01448508,  0.09273672],
                [-0.01115146, -0.00174601,  0.10427898],
                [-0.04050853, -0.00419696,  0.1125749 ],
                [ 0.01406789, -0.02773147,  0.06491844],
                [-0.006877, - 0.00438633,  0.11693656],
                [-0.05451076, -0.01365402, 0.06184569],
                [-0.02983921,  0.01176558,  0.09179644],
                [-0.02023908, -0.06952725, 0.06411217],
                [-0.01515248, -0.00403916, 0.08754122],
                [0.0072578, -0.00876088, 0.11302273],
                [0.00946499, -0.02391858, 0.07521297],
                [0.00423667, -0.00354773, 0.08419096],
                [0.00238491, -0.02353415, 0.08138207],
                [0.01292864, -0.03071827, 0.09525623],
                [0.0071115, 0.00660055, 0.09258613],
                [-0.0047571, 0.03009705, 0.10061671],
                [-0.01333719, -0.0334134, 0.0940367],
                [0.01743681, -0.03226607, 0.07954207],
                [0.00073329, 0.0012826, 0.1770344],
                [0.02515171, 0.0334027, 0.09304846],
                [0.01596735, 0.00797555, 0.09551173],
                [0.01673756, -0.03835148, 0.1225927],
                [0.00383512, -0.00991931, 0.09942244],
                [0.02707376, 0.00301628, 0.14303488],
                [0.05015839, 0.00474682, 0.11592135],
                [-0.00717502, -0.01034237, 0.05871968],
                [-0.03056454, 0.02745843, 0.12232597],
                [0.02438242, 0.02552895, 0.12512015],
                [0.00236241, 0.00020562, 0.10904837],
                [-0.00723518, -0.08869744, 0.04632035],
                [0.03614704, -0.00117987, 0.11866669],
                [0.00718681, -0.01377841, 0.08908521],
                [0.04863501, -0.00027613, 0.1099513],
                [-0.0176781, 0.0096269, 0.06136279],
                [-0.01979487, -0.07694364, -0.01696358],
                [-0.02870525, -0.02788106, 0.05403559],
                [0.01644892, -0.01420782, 0.0657668],
                [0.00329969, -0.00500166, 0.09796378],
                [-0.01010659, 0.02455958, 0.13142228],
                [0.02784512, -0.0199194, 0.09146485],
                [-0.00811078, -0.03215345, 0.08420132],
                [-0.01660325, -0.01308279, 0.1316551],
                [0.02517603, -0.0013262, 0.10214764],
                [0.01015503, 0.00323556, 0.09167695],
                [-0.0207515, -0.01136374, 0.0903455],
                [-0.00291848, 0.00805064, 0.10244771],
                [0.02321372, 0.00172258, 0.11346069],
                [-0.03602173, -0.00635536, 0.09453884],
                [0.00052262, -0.01366763, 0.09852844],
                [-0.02058481, 0.0141381, 0.1488167],
                [0.000884, -0.00310863, 0.09870237],
                [-0.00603949, 0.00969876, 0.09771967],
                [-0.00062998, 0.00055421, 0.10652353],
                [-0.00078606, -0.01708405, 0.10403484],
                [0.00415868, -0.03008506, 0.10914576],
                [-0.00119839, -0.06443124, 0.06130118],
                [0.00808375, -0.00824932, 0.0816161],
                [0.01583371, 0.01692427, 0.09424848],
                [0.00305598, -0.04932236, 0.06131371],
                [-0.01906054, -0.03026939, 0.06913354],
                [-0.00694686, -0.02286345, 0.09538428],
                [0.00206641, 0.00760575, 0.11231568],
                [-0.01212391, -0.00181662, 0.1108855],
                [0.0601216, 0.00943959, 0.1620444]]
valores_reales = [[0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                    [0.0, 0.0, 0.089159],
                 ]

print(len(valores_reales))
print(len(predicciones))
import csv
import numpy as np

# Convertir las listas a arreglos NumPy
datosp = np.array(predicciones)
datosv = np.array(valores_reales)

# Nombre del archivo CSV
nombre_archivo = 'art1.csv'

# Abrir el archivo CSV en modo escritura
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    # Crear un objeto escritor CSV
    escritor_csv = csv.writer(archivo_csv, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Escribir los encabezados en el archivo CSV
    escritor_csv.writerow(['xp', 'yp', 'zp', 'xv', 'yv', 'zv'])

    # Escribir los datos de las predicciones en el archivo CSV
    for dato in datosp:
        escritor_csv.writerow([dato[0], dato[1], dato[2], 0, 0, 0])

    # Escribir los datos de los valores reales en el archivo CSV
    for dato in datosv:
        escritor_csv.writerow([0, 0, 0, dato[0], dato[1], dato[2]])