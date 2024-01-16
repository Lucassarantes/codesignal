def solution(s):
    letters = ''
    
    i = 0
    
    while i < len(s):
        
        count = 1
        j = i +1
        
        while j < len(s) and s[i] == s[j]:
            count += 1
            j += 1
            
        letters += str(count) + s[i] if count > 1 else s[i]
        
        i = j
    return letters
