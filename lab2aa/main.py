from utils import *
    
sizes = [100, 500, 1000, 5000, 10000, 20000, 100000]
results = {
    "Quick Sort": [],
    "Merge Sort": [],
    "Heap Sort": [],
    "Radix Sort": []
}

for size in sizes:
    arr = generate_random_array(size)
    results["Quick Sort"].append(measure_execution_time(lambda arr: quick_sort(arr, 0, len(arr) - 1), arr))
    results["Merge Sort"].append(measure_execution_time(merge_sort, arr))
    results["Heap Sort"].append(measure_execution_time(lambda arr: heap_sort(arr), arr))
    results["Radix Sort"].append(measure_execution_time(radix_sort, arr))

plt.figure(figsize=(10, 5))
for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)
plt.xlabel("Array Size")
plt.ylabel("Execution Time (ms)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid()
plt.show()

arraySize = 50
arr = generate_random_array(arraySize)
visualize_sorting(merge_sort_visual, arr)  # Change to quick_sort if needed