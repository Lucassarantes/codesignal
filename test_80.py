def solution(a, b):
    count_ones = 0

    for num in range(a, b + 1):
        count_ones += bin(num).count('1')

    return count_ones
