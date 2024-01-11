def solution(min1, min2_10, min11, s):
    total_duration = 0
    
    for minute in range(1, s + 1):
        if minute == 1:
            cost = min1
        elif 2 <= minute <= 10:
            cost = min2_10
        else:
            cost = min11
        
        if s >= cost:
            total_duration += 1
            s -= cost
        else:
            break
    
    return total_duration
