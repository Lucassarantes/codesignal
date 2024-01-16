def solution(s1, s2):
    common_values = sum(min(s1.count(char), s2.count(char)) for char in set(s1))
    return common_values
