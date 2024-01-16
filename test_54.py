import re
from datetime import datetime

def solution(time):
    if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', time):
        datetime.strptime(time, '%H:%M')
        return True
    return False
