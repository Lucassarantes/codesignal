def solution(inputString):
    parts = inputString.split(".")
    if len(parts) != 4:
        return False
    print(inputString)
    for part in parts:
        if part == "" or not part.isdigit() or int(part) > 255 or int(part) < 0 or two_digits_less_than_ten(part):
            return False
    return True

def two_digits_less_than_ten(string):
    return len(string) > 1 and int(string) < 10