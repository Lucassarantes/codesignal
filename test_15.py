def solution(picture):
    result = []
    size = len(picture[0]) + 2
    asteriskis = ""
    for i in range(size):
        asteriskis += "*"
        
    result.append(asteriskis)
    for i in range(len(picture)):
        stringWithAst = "*"+picture[i]+"*"
        result.append(stringWithAst)
        
    result.append(asteriskis)
    return result
