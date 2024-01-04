def solution(statues):
    sorted_statues = sorted(statues)
    total = 0
    
    for i in range(len(sorted_statues) - 1):
        if (sorted_statues[i + 1] - sorted_statues[i]) > 1:
            total += (sorted_statues[i + 1] - sorted_statues[i])-1
    return total
