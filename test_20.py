def solution(inputArray):
    max_absolute = 0
    for i in range(1, len(inputArray)):
        absolute = abs(inputArray[i - 1] - inputArray[i])
        if max_absolute < absolute:
            max_absolute = absolute
    return max_absolute
