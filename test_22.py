def solution(inputArray):
    coordinates = sorted(inputArray)
    jump = 1
    while True:
        jumping = True
        for obstacle in coordinates:
            if obstacle % jump == 0:
                jumping = False
                break
        if jumping:
            return jump
        jump += 1
    
    
