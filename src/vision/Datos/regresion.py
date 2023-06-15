import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
y_true = [0.847771872, 0.84861, 0.849366, 0.8494915, 0.84307117, 0.821872, 0.83861, 0.829366, 0.8394915, 0.82307117]
y_pred = [0.84035, 0.854, 0.843, 0.84023, 0.84565, 0.82335, 0.8354, 0.83005, 0.8356, 0.826565]

# Calcular la línea de tendencia
slope, intercept = np.polyfit(y_true, y_pred, 1)
line_x = np.array([min(y_true), max(y_true)])
line_y = slope * line_x + intercept

# Graficar los puntos de regresión y la línea de tendencia
plt.scatter(y_true, y_pred)
plt.plot(line_x, line_y, color='red')

# Configurar la leyenda y las etiquetas de los ejes
# plt.legend(['Línea de tendencia', 'Puntos de regresión'])
plt.xlabel('Valores verdaderos')

plt.ylabel('Valores predecidos')

# Mostrar el gráfico
plt.show()