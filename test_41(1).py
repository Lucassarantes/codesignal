def solution(n):
    count = 0
    while True:
        digits = 0
        n_str = str(n)
        if n < 10:
            return count
        for digit in n_str:
            digits += int(digit)
        count += 1
        n = digits
        n_str = str(n)
