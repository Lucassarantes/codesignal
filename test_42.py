def solution(bishop, pawn):
    col = abs(ord(bishop[0]) - ord(pawn[0]))
    line = abs(int(bishop[1]) - int(pawn[1]))
    
    return col == line