def solution(st):
    reversed_st = st[::-1]
    
    if st == reversed_st:
        return st

    palindromes = []
    
    for i in range(1, len(reversed_st) + 1):
        reversed_param = st + reversed_st[i:]
        if reversed_param == ''.join(reversed(reversed_param)):
            palindromes.append(reversed_param)
    return min(palindromes, key=len)