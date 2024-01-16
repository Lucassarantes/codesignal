def solution(n, firstNumber):
    divisor = n / 2
    if firstNumber < divisor:
        return int(firstNumber) + divisor
    else:
        return int(firstNumber) - divisor
