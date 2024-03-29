def solution(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    
    while height < desiredHeight:
        height += upSpeed
        days += 1
        
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days