import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
size = 50
density = 0.2

def initialize_grid(size, density=0.2):
    grid = np.random.choice([OFF, ON], size=(size, size), p=[1 - density, density])
    return grid

def update(frameNum, img, grid, size):
    newGrid = grid.copy()

    for i in range(size):
        for j in range(size):
            total = int((grid[i, (j-1)%size] + grid[i, (j+1)%size] +
                         grid[(i-1)%size, j] + grid[(i+1)%size, j] +
                         grid[(i-1)%size, (j-1)%size] + grid[(i-1)%size, (j+1)%size] +
                         grid[(i+1)%size, (j-1)%size] + grid[(i+1)%size, (j+1)%size])/ON)

            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Initialisation de la grille
grid = initialize_grid(size, density)

# Configuration de l'affichage
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, size), frames=10, interval=200, save_count=50)

plt.show()
