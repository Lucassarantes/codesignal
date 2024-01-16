def solution(n, m):
    i = n
    total = 0
    while  m > 0:
        if m - n < 0:
            return total
        total += n
        m -= n
    return total
