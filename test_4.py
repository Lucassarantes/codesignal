def solution(inputArray):
    largest = None
    for i in range(len(inputArray)):
        if i < len(inputArray) - 1:
            product = inputArray[i] * inputArray[i + 1]
            if largest != None:
                if product > largest:
                    largest = product
            elif largest == None:
                largest = product
    return largest
