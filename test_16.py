def solution(a, b):
    if len(a) != len(b):
        return False

    if str(a) == str(b):
        return True
    
    diff = []

    for i in range(len(a)):
        if a[i] != b[i]:
            diff.append(i)

    if len(diff) > 2:
      return False
      
    if len(diff) == 2:
        [index1, index2] = diff
            
        return a[index1] == b[index2] and a[index2] == b[index1]

    return False
