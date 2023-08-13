def quickSort(arr, left, right):
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    i = left
    j = left + 1
    pivot = left
    while j <= right:
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[pivot], arr[i] = arr[i], arr[pivot]
    return i

import random

for i in range(100):
    arr = [random.randint(-100, 100) for _ in range(10)]
    res1 = sorted(arr)
    res2 = quickSort(arr, 0, len(arr)-1)
    if (res1==res2)== False:
        print(arr)
