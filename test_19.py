def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourRight == friendsRight:
        if yourLeft == friendsLeft:
            return True
    elif yourRight == friendsLeft:
        if yourLeft == friendsRight:
            return True
    return False