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

def generate_array(size, content_type):
    """Generate an array of a given size and content type"""
    if content_type == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    
    elif content_type == "sorted":
        return list(range(size))
    
    elif content_type == "reverse_sorted":
        return list(range(size, 0, -1))
    
    elif content_type == "partially_sorted":
        arr = list(range(size))
        # Shuffle a small portion of the array
        for i in range(size // 5):  # shuffle 20% of the array
            arr[random.randint(0, size-1)] = random.randint(0, 10000)
        return arr
    
    elif content_type == "partially_reverse_sorted":
        arr = list(range(size, 0, -1))
        # Shuffle a small portion of the array
        for i in range(size // 5):  # shuffle 20% of the array
            arr[random.randint(0, size-1)] = random.randint(0, 10000)
        return arr
    
    elif content_type == "duplicates":
        return [random.choice([random.randint(0, 1000), random.randint(0, 10)]) for _ in range(size)]
    
    elif content_type == "float_numbers":
        return [round(random.uniform(0, 1000), 2) for _ in range(size)]
    
    elif content_type == "negative_numbers":
        return [random.randint(-10000, 10000) for _ in range(size)]

def generate_datasets():
    """Generate the datasets for different sizes and content types"""
    sizes = {
        "XS": 100,
        "S": 500,
        "M": 1000,
        "L": 5000,
        "XL": 10000,
        "XXL": 20000,
        "XXXL": 100000
    }
    
    content_types = [
        "random", "sorted", "reverse_sorted", "partially_sorted", "partially_reverse_sorted",
        "duplicates", 
        "float_numbers", 
        "negative_numbers"
    ]
    
    datasets = {}
    
    for size_label, size in sizes.items():
        datasets[size_label] = {}
        for content_type in content_types:
            datasets[size_label][content_type] = generate_array(size, content_type)
    
    return datasets

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
