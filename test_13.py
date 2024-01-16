def solution(inputString):
    stack = []

    for i in range(len(inputString)):
        if inputString[i] == ')':
            reversedSubstring = ''

            while len(stack) > 0 and stack[len(stack) - 1] != '(':
                reversedSubstring += stack.pop()


      
            if len(stack) > 0 and stack[len(stack) - 1] == '(':
                stack.pop()
            
            for j in range(len(reversedSubstring)):
                stack.append(reversedSubstring[j])
        else:
            stack.append(inputString[i])
    return ''.join(stack)

