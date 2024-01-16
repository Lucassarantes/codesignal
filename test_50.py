def solution(s):
    letters = ''
    i = 0
    while i < len(s):
        count_letters = 1
        j = i + 1
        
        while j < len(s) and s[i] == s[j]:
            count_letters += 1
            j += 1
            
        if count_letters > 1:
            letters += str(count_letters) + s[i]
        else: 
            letters += s[i]
                
        i = j
        
    return letters
