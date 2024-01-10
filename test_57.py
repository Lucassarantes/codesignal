def solution(product):
    count = 1
    while count < 100000:
        digits_product = 1
        
        for digit in str(count):
            digits_product *= int(digit)
        
        if digits_product == product:
            return count
        count += 1
        
    return -1