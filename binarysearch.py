def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sample array (must be sorted)
array = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
index = binary_search(array, target)
print(f"Binary Search: {target} found at index {index}")