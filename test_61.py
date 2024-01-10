def solution(grid):
    def is_valid_set(nums):
        seen = set()
        for num in nums:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    for row in grid:
        if not is_valid_set(row):
            return False

    for col in zip(*grid):
        if not is_valid_set(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_grid = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_set(sub_grid):
                return False

    return True
