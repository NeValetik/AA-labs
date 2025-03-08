from utils import *

# Array sizes for experimentation
sizes = ["XS", "S", "M", "L", "XL", "XXL"]

# Create a dictionary to hold results for each sorting algorithm
results = {
    "Quick Sort": [],
    "Merge Sort": [],
    "Heap Sort": [],
    "Radix Sort": []
}

# Generate datasets with various content types
datasets = generate_datasets()

# Measure the execution time for sorting each dataset
for size in sizes:
    # Initialize lists to store execution times for each sorting algorithm
    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []
    radix_sort_times = []

    for content_type in datasets[size]:  # Loop through each content type for the current size
        arr = datasets[size][content_type]
        
        # Measure execution time for each sorting algorithm and add to corresponding lists
        quick_sort_times.append(measure_execution_time(lambda arr: quick_sort(arr, 0, len(arr) - 1), arr))
        merge_sort_times.append(measure_execution_time(merge_sort, arr))
        heap_sort_times.append(measure_execution_time(lambda arr: heap_sort(arr), arr))
        radix_sort_times.append(measure_execution_time(radix_sort, arr))

    # Compute the average execution time for each algorithm for the current size
    results["Quick Sort"].append(np.mean(quick_sort_times))
    results["Merge Sort"].append(np.mean(merge_sort_times))
    results["Heap Sort"].append(np.mean(heap_sort_times))
    results["Radix Sort"].append(np.mean(radix_sort_times))

# Plot the execution times for sorting algorithms based on array size
plt.figure(figsize=(10, 5))
for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)
plt.xlabel("Array Size")
plt.ylabel("Execution Time (ms)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid()
plt.show()

for content_type in datasets["XS"]:  # Loop through each content type in XS (same logic applies for "S" or "M")
    plt.figure(figsize=(10, 5))  # Create a new figure for each content type
    for name in results.keys():
        times = []  # List to store execution times for each size for the current algorithm

        for size in sizes:
            arr = datasets[size][content_type]
            # Measure execution time for the current sorting algorithm and add to list
            if name == "Quick Sort":
                times.append(measure_execution_time(lambda arr: quick_sort(arr, 0, len(arr) - 1), arr))
            elif name == "Merge Sort":
                times.append(measure_execution_time(merge_sort, arr))
            elif name == "Heap Sort":
                times.append(measure_execution_time(lambda arr: heap_sort(arr), arr))
            elif name == "Radix Sort":
                times.append(measure_execution_time(radix_sort, arr))

        # Plot the execution times for the current algorithm for the current content type
        plt.plot(sizes, times, marker='o', label=name)
    
    # Set plot labels and title
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (ms)")
    plt.title(f"Sorting Algorithm Performance for {content_type.capitalize()} Content")
    plt.legend()
    plt.grid()
    plt.show()

arr = datasets["XS"]["random"]
visualize_sorting(merge_sort_visual, arr)