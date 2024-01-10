import re

def solution(inputString):
    mac = inputString.split("-")
    for group in mac:
        if len(group) > 2 or len(group) < 2:
            return False
        if not group.isdigit():
            for char in group:
                if not char.isdigit() and re.match(r'^[a-fA-F]$', char) is None:
                    return False
    return True