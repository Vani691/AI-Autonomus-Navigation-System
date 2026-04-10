import matplotlib.pyplot as plt
import numpy as np

def plot_path(path, start, goal):
    path = np.array(path)

    plt.figure(figsize=(6,6))

    # Color gradient
    colors = np.linspace(0, 1, len(path))

    plt.scatter(path[:,1], path[:,0], c=colors, cmap='plasma', s=50)

    # Start & Goal
    plt.scatter(start[1], start[0], color='green', s=100, label='Start')
    plt.scatter(goal[1], goal[0], color='red', s=100, label='Goal')

    plt.gca().invert_yaxis()
    plt.title("Path Visualization (Step-wise)")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/path_visualization.png")
    plt.show()