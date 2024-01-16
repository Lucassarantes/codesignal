def solution(inputString):
    inputString = sorted(list(inputString))
    if inputString[0] != "a":
        return False

    input_set = sorted(set(inputString))
    
    counted_letters = []

    for char in input_set:
        counted_letters.append(inputString.count(char))
        
    print 
    for i in range(len(counted_letters) - 1):
        if counted_letters[i] < counted_letters[i + 1] or int(ord(input_set[i + 1])) - int(ord(input_set[i])) != 1:
            return False
    return True