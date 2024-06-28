import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
target = 30
result = jump_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")