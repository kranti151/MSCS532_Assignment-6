"""
Assignment 6 - Selection Algorithms
Komalben Suthar

"""

import random
import time


# ------------------------------
# Randomized Quickselect
# ------------------------------

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def randomized_quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_quickselect(arr, low, pivot_index - 1, k)
    else:
        return randomized_quickselect(arr, pivot_index + 1, high, k)


# ------------------------------
# Median of Medians (Deterministic)
# ------------------------------

def partition(arr, pivot):
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return left, middle, right


def median_of_medians(arr, k):

    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = [sorted(group)[len(group)//2] for group in groups]

    pivot = median_of_medians(medians, len(medians)//2)

    left, middle, right = partition(arr, pivot)

    if k < len(left):
        return median_of_medians(left, k)

    elif k < len(left) + len(middle):
        return pivot

    else:
        return median_of_medians(right, k - len(left) - len(middle))


# ------------------------------
# Benchmarking
# ------------------------------

def benchmark():

    sizes = [1000, 5000, 10000]

    for n in sizes:

        arr = [random.randint(1, n) for _ in range(n)]
        k = n // 2

        start = time.time()
        randomized_quickselect(arr.copy(), 0, n-1, k)
        t1 = time.time() - start

        start = time.time()
        median_of_medians(arr.copy(), k)
        t2 = time.time() - start

        print(f"\nArray size: {n}")
        print("Randomized Quickselect:", t1)
        print("Median of Medians:", t2)


if __name__ == "__main__":
    benchmark()