def solution(n):
    nstring = str(n)
    
    if len(nstring) % 2 != 0:
        return False
        
    firstHalf = 0
    secondHalf = 0
    
    counter = len(nstring) - 1

    for i in range(int(len(nstring) / 2)):
        firstHalf += int(nstring[i])
        secondHalf += int(nstring[counter])
        counter -= 1

    if firstHalf == secondHalf:
        return True
    else:
        return False
