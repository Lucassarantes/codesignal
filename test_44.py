from collections import Counter

def solution(inputString):
    if 'a' not in inputString:
        return False
    
    timesAppeared = Counter(inputString)

    unique_letters = ''.join(sorted(set(timesAppeared.keys())))

    for i in range(len(unique_letters) - 1):
        if timesAppeared[unique_letters[i]] < timesAppeared[unique_letters[i + 1]] or ord(unique_letters[i]) - ord(unique_letters[i + 1]) != -1:
            return False

    return True