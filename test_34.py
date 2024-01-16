def solution(inputArray, k):
    return [value for index, value in enumerate(inputArray, start=1) if index % k != 0]
