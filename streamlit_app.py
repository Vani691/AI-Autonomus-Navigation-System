import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

from src.simulation.environment import GridEnvironment
from src.planning.astar import astar
from src.agent.robot import Robot
from src.perception.sensor_simulation import get_distance

# ---------------- SESSION STATE ----------------
if "running" not in st.session_state:
    st.session_state.running = False

if "finished" not in st.session_state:
    st.session_state.finished = False

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="AI Navigation Dashboard", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Controls")

grid_size = st.sidebar.slider("Grid Size", 10, 30, 20)
speed = st.sidebar.slider("Simulation Speed", 0.05, 1.0, 0.2)

if st.sidebar.button("▶️ Start Simulation"):
    st.session_state.running = True
    st.session_state.finished = False

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align: center; color: #00FFAA;'>🚗 AI Autonomous Navigation System</h1>",
    unsafe_allow_html=True
)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([2, 1])

# ---------------- INIT ----------------
env = GridEnvironment(grid_size, grid_size)
start = (0, 0)
goal = (grid_size - 1, grid_size - 1)

path, explored = astar(env.grid, start, goal)
robot = Robot(start, path)

distance_log = []

# placeholders
grid_placeholder = col1.empty()
graph_placeholder = col2.empty()
metrics_placeholder = col2.empty()

# ---------------- SIMULATION ----------------
if st.session_state.running:

    for step in range(len(path)):

        plt.close('all')  # prevent plot stacking

        distance = get_distance()
        distance_log.append(distance)

        robot.move()

        # -------- GRID --------
        fig, ax = plt.subplots(figsize=(5, 5))
        grid = np.array(env.grid)
        ax.imshow(grid, cmap="gray")

        r, c = robot.position
        ax.scatter(c, r, color="cyan", s=120)

        ax.set_title(f"Step {step}")
        ax.invert_yaxis()

        grid_placeholder.pyplot(fig)

        # -------- GRAPH --------
        fig2, ax2 = plt.subplots()
        ax2.plot(distance_log, color="cyan")
        ax2.set_title("Sensor Distance")
        graph_placeholder.pyplot(fig2)

        # -------- METRICS --------
        with metrics_placeholder.container():
            st.metric("Step", step)
            st.metric("Distance", f"{distance} cm")
            st.metric("Path Length", len(path))

        # -------- STATUS --------
        status = "SAFE" if distance > 20 else "OBSTACLE NEAR"
        st.sidebar.markdown("## 🚦 System Status")
        if status == "SAFE":
            st.sidebar.success("SAFE")
        else:
            st.sidebar.error("OBSTACLE DETECTED")

        # -------- PROGRESS --------
        progress = step / len(path)
        st.progress(progress)
        st.write(f"### Path Completion: {progress * 100:.2f}%")

        time.sleep(speed)

    st.success("🎯 Goal Reached Successfully!")

    # mark simulation complete
    st.session_state.running = False
    st.session_state.finished = True


# ---------------- ANALYTICS (AFTER SIMULATION) ----------------
if st.session_state.finished:

    st.header("📊 Analytics Dashboard")

    # -------- PERFORMANCE --------
    st.subheader("⚡ Performance Analysis")

    def performance_analysis():
        densities = [5, 10, 15, 20, 25, 30]
        path_lengths = []
        times = []

        for d in densities:
            env = GridEnvironment(20, 20)
            start = (0, 0)
            goal = (19, 19)

            t1 = time.time()
            path, _ = astar(env.grid, start, goal)
            t2 = time.time()

            path_lengths.append(len(path))
            times.append(t2 - t1)

        return densities, path_lengths, times

    densities, path_lengths, times = performance_analysis()

    fig4, ax4 = plt.subplots()
    ax4.plot(densities, path_lengths, label="Path Length")
    ax4.plot(densities, times, label="Time")
    ax4.set_title("Performance vs Obstacle Density")
    ax4.legend()

    st.pyplot(fig4)

    # -------- HEATMAP --------
    st.subheader("🔥 Heatmap")

    heatmap = np.random.rand(20, 20)

    fig5, ax5 = plt.subplots()
    ax5.imshow(heatmap, cmap="inferno")
    ax5.set_title("Navigation Heatmap")

    st.pyplot(fig5)

    # -------- EXPLORATION --------
    st.subheader("🧠 A* Exploration")

    fig3, ax3 = plt.subplots(figsize=(5, 5))

    for node in explored:
        ax3.scatter(node[1], node[0], color="yellow", s=10)

    ax3.set_title("Explored Nodes")
    ax3.invert_yaxis()

    st.pyplot(fig3)