import re

def solution(name):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    if name[0].isdigit() or name[0] == " ":
        return False
        
    return bool(pattern.match(name))