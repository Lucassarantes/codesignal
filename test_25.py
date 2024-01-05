def solution(inputArray, elemToReplace, substitutionElem):
    return list(map(lambda el: substitutionElem if el == elemToReplace else el, inputArray))
