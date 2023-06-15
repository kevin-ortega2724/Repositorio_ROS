import numpy as np
from scipy.spatial.transform import Rotation as R
import csv

def ur5_direct_kinematics(q):
    # Longitudes de los eslabones
    a = [0, -0.425, -0.39225, 0, 0, 0]
    # Desplazamientos de los eslabones
    d = [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
    # Ángulos alpha
    alpha = [np.pi / 2, 0, 0, np.pi / 2, -np.pi / 2, 0]

    # Matrices de transformación homogénea
    T = []
    for i in range(6):
        T.append(np.array([
            [np.cos(q[i]), -np.sin(q[i]) * np.cos(alpha[i]), np.sin(q[i]) * np.sin(alpha[i]), a[i] * np.cos(q[i])],
            [np.sin(q[i]), np.cos(q[i]) * np.cos(alpha[i]), -np.cos(q[i]) * np.sin(alpha[i]), a[i] * np.sin(q[i])],
            [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
            [0, 0, 0, 1]
        ]))

    # Matrices de transformación homogénea para cada eslabón
    T_01 = T[0]
    T_02 = T_01 @ T[1]
    T_03 = T_02 @ T[2]
    T_04 = T_03 @ T[3]
    T_05 = T_04 @ T[4]
    T_06 = T_05 @ T[5]

    # Obtener los valores de posición y orientación de cada eslabón
    p_0 = np.array([0, 0, 0, 1])
    p_1 = T_01 @ p_0
    p_2 = T_02 @ p_0
    p_3 = T_03 @ p_0
    p_4 = T_04 @ p_0
    p_5 = T_05 @ p_0
    p_6 = T_06 @ p_0

    R_0 = np.eye(3)
    R_1 = T_01[:3, :3]
    R_2 = T_02[:3, :3]
    R_3 = T_03[:3, :3]
    R_4 = T_04[:3, :3]
    R_5 = T_05[:3, :3]
    R_6 = T_06[:3, :3]

    return [T_01, T_02, T_03, T_04, T_05, T_06], [p_0[:3], p_1[:3], p_2[:3], p_3[:3], p_4[:3], p_5[:3], p_6[:3]], [R.from_matrix(R_0), R.from_matrix(R_1), R.from_matrix(R_2), R.from_matrix(R_3), R.from_matrix(R_4), R.from_matrix(R_5), R.from_matrix(R_6)]


# Leer los ángulos desde un archivo CSV
with open('angulos.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Omitir la primera fila del archivo CSV
    q_list = list(reader)

# Convertir los ángulos a números de punto flotante
q_list = [[float(q) for q in row] for row in q_list]


# Calcular la cinemática directa para cada configuración de articulaciones
with open('datosapi.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['px6', 'py6', 'pz6', 'α6', 'β6', 'γ6', 'qz6', 'px5', 'py5', 'pz5', 'α5', 'β5', 'γ5', 'px4', 'py4', 'pz4', 'α4', 'β4', 'γ4', 'px3', 'py3', 'pz3', 'α3', 'β3', 'γ3', 'px2', 'py2', 'pz2','α2', 'β2', 'γ2', 'px1', 'py1', 'pz1', 'α1', 'β1', 'γ1'])
    for q in q_list:
        T, p, Rz = ur5_direct_kinematics(q)

        # Escribir los valores de posición y orientación en una sola fila para cada eslabón
        row = []
        for i in range(7):
            px, py, pz = p[i]
            roll, pitch, yaw = Rz[i].as_euler('zyx')
            # print(roll)
            row.extend([px, py, pz, roll, pitch, yaw])
        writer.writerow(row)
print("Los valores de posición y orientación se han guardado en el archivo posiciones.csv.")
for q in q_list:
    T, p, Rr = ur5_direct_kinematics(q)

    # Imprimir los valores de posición y orientación de cada eslabón
    for i in range(7):
        print('Coordenadas theta:', q)
        # print('algorit', T)
        print('Coordenadas theta en grados', np.degrees(q))
        print("Eslabón ", i, 'de', q)
        print("Valores de posición: x={:.3f}, y={:.3f}, z={:.3f}".format(p[i][0], p[i][1], p[i][2]))
        print("Valores de orientación (matriz de rotación): ")
        print(Rr[i].as_matrix())
        print("Valores de orientación (cuaternión): x={:.3f}, y={:.3f}, z={:.3f}, w={:.3f}".format(*Rr[i].as_quat()))
        print("Valores de orientación (ángulos de Euler): roll={:.3f}, pitch={:.3f}, yaw={:.3f}".format(*Rr[i].as_euler('zyx', degrees=True)))
        print(Rr[i].as_euler('zyx'))
        # print(roll[i])

