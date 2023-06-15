import numpy as np

# Definir la función de cinemática directa del robot arm de 6-DOF
def forward_kinematics(theta1, theta2, theta3, theta4, theta5, theta6):
    """Calcula la posición final del extremo del robot arm de 6-DOF dadas las 6 articulaciones."""
    # Definir los parámetros del brazo
    a1 = 0.5
    a2 = 0.4
    d1 = 0.2
    d5 = 0.1
    d6 = 0.05
    
    # Calcular las matrices de transformación homogénea para cada articulación
    T1 = np.array([
        [np.cos(theta1), 0, np.sin(theta1), 0],
        [np.sin(theta1), 0, -np.cos(theta1), 0],
        [0, 1, 0, d1],
        [0, 0, 0, 1]
    ])
    
    T2 = np.array([
        [np.cos(theta2), -np.sin(theta2), 0, a1*np.cos(theta2)],
        [np.sin(theta2), np.cos(theta2), 0, a1*np.sin(theta2)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    T3 = np.array([
        [np.cos(theta3), -np.sin(theta3), 0, a2*np.cos(theta3)],
        [np.sin(theta3), np.cos(theta3), 0, a2*np.sin(theta3)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    T4 = np.array([
        [np.cos(theta4), 0, np.sin(theta4), 0],
        [np.sin(theta4), 0, -np.cos(theta4), 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])
    
    T5 = np.array([
        [np.cos(theta5), 0, -np.sin(theta5), 0],
        [np.sin(theta5), 0, np.cos(theta5), 0],
        [0, -1, 0, d5],
        [0, 0, 0, 1]
    ])
    
    T6 = np.array([
        [np.cos(theta6), -np.sin(theta6), 0, 0],
        [np.sin(theta6), np.cos(theta6), 0, 0],
        [0, 0, 1, d6],
        [0, 0, 0, 1]
    ])
    
    # Combinar las transformaciones para obtener la matriz de transformación homogénea final
    T = T1 @ T2 @ T3 @ T4 @ T5 @ T6
    
    # Extraer la posición final del extremo del brazo
    x = T[0, 3]
    y = T[1, 3]
    z = T[2, 3]
    
    # Extraer los ángulos de Euler de la matriz de rotación
    sy = np.sqrt(T[0, 0]**2 + T[1, 0]**2)
    singular = sy < 1e-6
    
    if not singular:
        x = np.arctan2(T[2, 1], T[2, 2])
        y = np.arctan2(-T[2, 0], sy)
        z = np.arctan2(T[1, 0], T[0, 0])
    else:
        x = np.arctan2(-T[1, 2], T[1, 1])
        y = np.arctan2(-T[2, 0], sy)
        z = 0
    
    return np.array([x, y, z, theta4, theta5, theta6])
    
    """
    Aquí, estamos extrayendo los ángulos de Euler de la matriz de rotación. Primero, calculamos sy como la magnitud de los elementos T[0, 0] y T[1, 0]. Si sy es menor que un umbral muy pequeño (1e-6 en este caso), entonces la matriz de rotación es singular y no se puede extraer una solución única para los ángulos de Euler. En este caso, simplemente configuramos z a cero y calculamos x y y en consecuencia.

Si sy no es singular, entonces usamos las funciones arctan2 para calcular x, y y z a partir de los elementos de la matriz de rotación. La convención utilizada aquí es la siguiente: x representa el ángulo de rotación en torno al eje x, y representa el ángulo de rotación en torno al eje y, y z representa el ángulo de rotación en torno al eje z. Los ángulos se devuelven en un array numpy de seis elementos en el siguiente orden: [x, y, z, theta4, theta5, theta6].

Con esto, hemos completado la función de cinemática directa y la función de cinemática inversa para el robot arm de 6-DOF en Python.
    """
