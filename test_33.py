def solution(inputArray):
    return generate_arrangements(inputArray, 0)
            
def is_consecutive(arr):
    for i in range(len(arr) - 1):
        if sum(a != b for a, b in zip(arr[i], arr[i + 1])) != 1:
            return False
    return True
        
def generate_arrangements(arr, start):
    if start == len(arr):
        if is_consecutive(arr):
            return True
        return False
    
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        if generate_arrangements(arr, start + 1):
            return True
        arr[start], arr[i] = arr[i], arr[start]
    return False