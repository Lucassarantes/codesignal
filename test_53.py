import re

def solution(text):
    words = re.findall(r'[a-zA-Z]+', text)
    
    return max(words, key=len)