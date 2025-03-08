def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def quick_sort_visual(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = yield from partition_visual(arr, low, high)
        yield from quick_sort_visual(arr, low, pivot_index - 1)
        yield from quick_sort_visual(arr, pivot_index + 1, high)


def partition_visual(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr.copy()  # Yield array state after swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr.copy()  # Yield final partitioned state
    return i + 1


def merge_sort_visual(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort_visual(arr, start, mid)
        yield from merge_sort_visual(arr, mid, end)
        yield from merge_in_place_visual(arr, start, mid, end)


def merge_in_place_visual(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    
    i = j = 0
    k = start
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        yield arr.copy()  # Yield after every modification

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr.copy()

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr.copy()


def heapify_visual(arr, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        yield arr.copy()
        yield from heapify_visual(arr, n, largest)


def heap_sort_visual(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify_visual(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        yield arr.copy()
        yield from heapify_visual(arr, i, 0)


def counting_sort_visual(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
        yield arr.copy()  # Yield intermediate states


def radix_sort_visual(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        yield from counting_sort_visual(arr, exp)
        exp *= 10