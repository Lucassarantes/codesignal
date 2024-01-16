def solution(matrix):
    sum = 0
    
    for l in range(len(matrix)):
        for c in range(len(matrix[l])):
            if l == 0 and matrix[l][c] > 0:
                sum += matrix[l][c]
            elif matrix[l][c] > 0 and matrix[l - 1][c] > 0 and matrix[0][c] > 0:
                sum += matrix[l][c]
    return sum