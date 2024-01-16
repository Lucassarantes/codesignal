def solution(cell):
    col = ord(cell[0]) - ord("a") + 1
    row = int(cell[1])
    
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, -2), (-1, 2),
    ]
    
    valid_moves = 0
    
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            valid_moves += 1
        
    return valid_moves