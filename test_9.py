def solution(inputArray):
    if len(inputArray) == 1:
        return inputArray
    
    longest = len(max(inputArray, key=len))
    
    longest_items = [item for item in inputArray if len(item) == longest]
    
    return longest_items
