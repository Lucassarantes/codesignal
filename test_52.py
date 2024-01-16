def solution(n):
    n_str = str(n)
    numbers = []
    
    for i in range(len(n_str)):
        numbers.append(int(n_str[:i] + n_str[i+1:]))
        
    return max(numbers)
        