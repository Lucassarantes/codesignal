def solution(inputString):
    prefix = ""
    for char in inputString:
        if char.isdigit():
            prefix += char
        else:
            break
    return prefix