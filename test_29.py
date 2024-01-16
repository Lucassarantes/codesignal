def solution(cell1, cell2):
    row1, col1 = ord(cell1[0]) - ord('A'), int(cell1[1]) - 1
    row2, col2 = ord(cell2[0]) - ord('A'), int(cell2[1]) - 1

    # Check if the sum of indices is even or odd
    return (row1 + col1) % 2 == (row2 + col2) % 2