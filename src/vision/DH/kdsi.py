import numpy as np

def ur5_direct_kinematics(q):
    # Longitudes de los eslabones
    a = [0, -0.425, -0.39225, 0, 0, 0]
    # Desplazamientos de los eslabones
    d = [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
    # Ángulos alpha
    alpha = [-np.pi/2, 0, 0, -np.pi/2, np.pi/2, 0]
    
    # Matrices de transformación homogénea
    T = []
    for i in range(6):
        T.append(np.array([
            [np.cos(q[i]), -np.sin(q[i]) * np.cos(alpha[i]), np.sin(q[i]) * np.sin(alpha[i]), a[i] * np.cos(q[i])],
            [np.sin(q[i]), np.cos(q[i]) * np.cos(alpha[i]), -np.cos(q[i]) * np.sin(alpha[i]), a[i] * np.sin(q[i])],
            [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
            [0, 0, 0, 1]
        ]))
    
    # Matriz de transformación homogénea total
    T_06 = T[0] @ T[1] @ T[2] @ T[3] @ T[4] @ T[5]
    
    return T_06
# Calcular la cinemática directa para la configuración de las articulaciones dada
q = [0, 0, 0, 0, 0, 0]
T_06 = ur5_direct_kinematics(q)
print(T_06)
# Obtener los valores de posición y orientación del efector final
p = T_06[:3, 3]
R = T_06[:3, :3]

print("Valores de posición: ", p)
print("Valores de orientación: \n", R)

