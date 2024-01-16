def solution(inputString):
    parts = inputString.split("-")
    
    if len(parts) != 6:
        return False
        
    for part in parts:
        if len(part) != 2:
            return False
        try:
            if not (0 <= int(part, 16) <= 255):
                return False
        except ValueError:
            return False
            
    return True