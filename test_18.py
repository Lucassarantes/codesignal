def solution(inputString):
    charCount = {}
    oddCount = 0

    for char in inputString:
        charCount[char] = charCount.get(char, 0) + 1

    for count in charCount.values():
        if count % 2 != 0:
            oddCount += 1

    return oddCount <= 1
