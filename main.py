import pygame
from src.simulation.environment import GridEnvironment
from src.planning.astar import astar
from src.agent.robot import Robot
from src.analytics.visualizer import plot_path
from src.analytics.metrics import generate_heatmap, performance_graph

# Optional modules
from src.perception.sensor_simulation import get_distance
# from src.perception.camera import get_frame
# from src.perception.object_detection import ObjectDetector

def main():
    pygame.init()

    env = GridEnvironment(20, 20)
    start = (0, 0)
    goal = (19, 19)

    path = astar(env.grid, start, goal)
    robot = Robot(start, path)

    plot_path(path, start, goal)
    generate_heatmap(env.grid)
    performance_graph()

    # detector = ObjectDetector()

    running = True
    clock = pygame.time.Clock()

    while running:
        env.draw()

        # 🔹 Simulated sensor input
        distance = get_distance()
        print(f"Simulated Distance: {distance} cm")

        if distance < 20:
            env.update_from_sensor()

        #  camera + detection
        """
        frame = get_frame()
        if frame is not None:
            objects = detector.detect(frame)
            print("Detected:", objects)
        """

        robot.move()
        robot.draw(env.screen)

        # 🏁 STOP CONDITION: Check if robot reached the goal
        if robot.position == goal:
            print("Goal Reached! Ending simulation...")
            env.draw()             # Final draw to show robot at goal
            robot.draw(env.screen)
            pygame.display.flip()
            pygame.time.wait(2000) # Wait 2 seconds so you can see the finish
            running = False        # Exit the loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()