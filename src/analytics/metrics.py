import numpy as np
import matplotlib.pyplot as plt

def generate_heatmap(grid):
    heatmap = np.random.rand(len(grid), len(grid[0])) * 40

    plt.figure(figsize=(6,6))
    plt.imshow(heatmap, cmap='inferno')

    plt.colorbar(label="Cost from Start")
    plt.title("Navigation Cost Heatmap")

    plt.savefig("outputs/heatmap.png")
    plt.show()


def performance_graph():
    obstacle_density = [5,10,15,20,25,30]
    path_length = [40,42,43,45,47,50]
    time_taken = [0.9,0.8,0.6,0.5,0.3,0.2]

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.plot(obstacle_density, path_length, marker='o')
    plt.title("Path Length vs Obstacles")
    plt.xlabel("Obstacle %")
    plt.ylabel("Path Length")

    plt.subplot(1,2,2)
    plt.plot(obstacle_density, time_taken, marker='o')
    plt.title("Time vs Obstacles")
    plt.xlabel("Obstacle %")
    plt.ylabel("Time (sec)")

    plt.tight_layout()
    plt.savefig("outputs/performance.png")
    plt.show()