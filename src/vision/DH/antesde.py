#Lo que va antes de la función, guardar



# Parámetros DH del robot UR5
d1, a2, a3, d4, d5, d6 = 0.089159, -0.425, -0.39225, 0.10915, 0.09465, 0.0823
T = np.array([[ 1.000000e+00,  0.000000e+00,  0.000000e+00, -8.172500e-01],
 [ 0.000000e+00, 6.123234e-17,  1.000000e+00,  1.914500e-01],
 [ 0.000000e+00, -1.000000e+00,  6.123234e-17, -5.491000e-03],
 [ 0.000000e+00,  0.000000e+00,  0.000000e+00,  1.000000e+00]])
print(T)

def UR5_IK(T):
    """
    Función que realiza la cinemática inversa del robot UR5.

    Parámetros:
    T -- matriz de transformación homogénea que describe la posición y orientación del extremo del robot

    Devuelve:
    q -- lista con las coordenadas articulares del robot [q1, q2, q3, q4, q5, q6]
    """

    # Obtenemos la posición del extremo del robot a partir de la matriz de transformación homogénea
    p = T[:3, 3]

    # Obtenemos la orientación del extremo del robot a partir de la matriz de transformación homogénea
    R = T[:3, :3]

    # Obtenemos la orientación de la muñeca del robot (el eslabón 4) a partir de la orientación del extremo
    R3 = R[:, 2]

    # Calculamos el valor de q1
    q1 = atan2(p[1], p[0])

    # Calculamos el valor de q3
    D = (p[0]**2 + p[1]**2 + (p[2]-d1)**2 - a2**2 - a3**2) / (2*a2*a3)
    D = max(min(D, 1), -1)
    q3 = atan2(-sqrt(1-D**2), D)

    # Calculamos el valor de q2
    K1 = a2 + a3*D
    K2 = a3*sqrt(1-D**2)
    theta = atan2((p[2]-d1), sqrt(p[0]**2 + p[1]**2))
    q2 = atan2(K1*p[1] - K2*np.cos(theta), K1*p[0] - K2*np.sin(theta))

    # Calculamos el valor de q4, q5 y q6
    R36 = np.linalg.inv(np.array([[np.cos(q1)*R[0,0] + np.sin(q1)*R[1,0], np.cos(q1)*R[0,1] + np.sin(q1)*R[1,1], np.cos(q1)*R[0,2] + np.sin(q1)*R[1,2]],
                                  [-np.sin(q1)*R[0,0] + np.cos(q1)*R[1,0], -np.sin(q1)*R[0,1] + np.cos(q1)*R[1,1], -np.sin(q1)*R[0,2] + np.cos(q1)*R[1,2]],
                                  [R[2,0], R[2,1], R[2,2]]]))
    q5 = atan2(sqrt(R36[2, 0]**2 + R36[2, 1]**2), R36[2, 2])
    q4 = atan2(R36[1, 2]/np.sin(q5), R36[0, 2]/np.sin(q5))
    q6 = atan2(R36[2, 1]/np.sin(q5), -R36[2, 0]/np.sin(q5))

    # Devolvemos la lista de coordenadas articulares calculadas
    q = [q1, q2, q3, q4, q5, q6]
    return q
# Calculamos las coordenadas articulares correspondientes a la matriz de transformación homogénea T
q = UR5_IK(T)

# Imprimimos las coordenadas articulares resultantes
print("aa",q)



