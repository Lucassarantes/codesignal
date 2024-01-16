def solution(deposit, rate, threshold):
    months = 0
    while deposit < threshold:
        deposit += deposit * (rate/100)
        months += 1
    return months
