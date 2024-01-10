def solution(st):
    if st == ''.join(reversed(st)):
        return st
        
    rev = ''.join(reversed(st))
    palindromes = []
    for i in range(1, len(rev) + 1):
        rev_param = rev[i:]
        if st+rev_param == ''.join(reversed(st + rev_param)):
            palindromes.append(st + rev_param)
    return min(palindromes, key=len)