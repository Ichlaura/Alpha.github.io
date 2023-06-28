import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear la figura y el objeto de la subparcela 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordenadas del cubo
x = [-1, 1, 1, -1, -1, 1, 1, -1]
y = [-1, -1, 1, 1, -1, -1, 1, 1]
z = [-1, -1, -1, -1, 1, 1, 1, 1]

# Función de actualización para animación
def update_frame(frame):
    ax.cla()  # Borrar el gráfico anterior
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Rotar el cubo en cada iteración
    angle = frame * 2  # Ajustar la velocidad de rotación
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    rotated_coords = np.dot(rotation_matrix, np.array([x, y, z]))
    ax.plot3D(rotated_coords[0], rotated_coords[1], rotated_coords[2])

# Crear la animación
animation = FuncAnimation(fig, update_frame, frames=np.arange(0, 100), interval=50)

# Mostrar la animación
plt.show()
