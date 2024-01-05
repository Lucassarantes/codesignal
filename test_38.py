def solution(inputArray, k):
    max_sum = sum(inputArray[:k])
    curr_sum = max_sum

    for i in range(1, len(inputArray) - k + 1):
        curr_sum = curr_sum - inputArray[i - 1] + inputArray[i + k - 1]
        max_sum = max(max_sum, curr_sum)

    return max_sum