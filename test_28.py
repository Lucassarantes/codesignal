def solution(inputString):
    result = ""
    for char in inputString:
        if char == 'z':
            result += 'a'
        else:
            result += chr(ord(char)+1)
    return result
    
