def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows < 2 or cols < 2:
        return 0
        
    squares = set()

    for i in range(rows - 1):
        for j in range(cols - 1):
            square = (
                matrix[i][j], matrix[i][j+1],
                matrix[i+1][j], matrix[i+1][j+1]
            )
            squares.add(tuple(square))

    return len(squares)
