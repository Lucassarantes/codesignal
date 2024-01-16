def solution(inputArray, k):
    max_sum = 0
    for i in range(len(inputArray) - k + 1):
        curr_sum = sum(inputArray[i:i+k])
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum
            
