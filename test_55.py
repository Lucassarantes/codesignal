import re

def solution(inputString):
      
    data = re.findall(r'\d+', inputString)
    return sum(int(digit) for digit in data)