def solution(inputArray):
    moves = 0;
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            moves += (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
    return moves
