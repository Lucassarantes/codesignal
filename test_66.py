def solution(divisor, bound):
    max_divisors = []
    count = bound
    while True:
        if count % divisor == 0:
            return count
        count -= 1
