import time
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sorts import *

def measure_execution_time(sort_function, array):
    start = time.perf_counter()
    sort_function(array.copy())
    end = time.perf_counter()
    return (end - start) * 1000  # Convert to milliseconds

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def visualize_sorting(sort_function, arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='edge')

    def update(frame):
        for bar, val in zip(bars, frame):
            bar.set_height(val)
        return bars

    generator = sort_function(arr)
    ani = animation.FuncAnimation(fig, update, frames=generator, repeat=False, blit=False, interval=50)

    plt.show()
