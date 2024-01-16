def solution(n):
    even = True
    numbers = str(n)
    for number in numbers:
        if int(number) % 2 != 0:
            even = False
    
    return even
