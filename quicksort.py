def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)



array = [5, 3, 8, 6, 2, 7, 4, 1]
sorted_array = quick_sort(array)
print("Quick Sort:", sorted_array)