def solution(a):
    minor = None
    min_sum = float("inf")
    
    for n in a:
        result = 0
        for n2 in a:
            result += abs(n2 - n)

        if result < min_sum:
            min_sum = result
            minor = n
    return minor
    
