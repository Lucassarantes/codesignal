def solution(year):
    calc_result =  year / 100
    if calc_result == int(calc_result):
        return calc_result
    elif calc_result > int(calc_result):
        return int(calc_result) + 1
