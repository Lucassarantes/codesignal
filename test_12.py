def solution(a):
    aux = 0
    
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] != -1 and a[j] != -1:
                if a[i] > a[j]:
                    aux = a[i]
                    a[i] = a[j]
                    a[j] = aux
    return a