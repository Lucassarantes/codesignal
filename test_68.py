def solution(n):
    hours = n // 60
    minutes = n % 60

    digit_sum = sum(map(int, str(hours) + str(minutes)))

    return digit_sum