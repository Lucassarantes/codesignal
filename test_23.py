def solution(image):
    blurred_image = []
    rows = len(image)
    cols = len(image[0])
    
    for i in range(1, rows - 1):
        row_result = []
        for j in range(1, cols - 1):
            row_result.append(sum(image[x][y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)) // 9)
        blurred_image.append(row_result)
    return blurred_image
