def solution(n):
    
    if len(str(n)) <= 1:
        return 0
        
    total = 0
    while n >= 10:
        n = sum(int(number) for number in str(n))
        total += 1
    return total