def solution(inputString):
    prefix = ''
    i = 0
    while i < len(inputString):
        if inputString[i].isdigit():
            prefix += inputString[i]
        else:
            return prefix
        i += 1
        
    return prefix