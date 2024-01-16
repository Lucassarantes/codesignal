def solution(inputString):
    palindrome = "";
    for letter in range(len(inputString), 0, -1):
        palindrome = palindrome + inputString[letter-1]
    print(palindrome)
    if palindrome == inputString:
        return True
    else:
        return False