def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        result[x][y] += 1
                result[i][j] -= 1

    return result
