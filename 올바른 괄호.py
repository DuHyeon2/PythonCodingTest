def solution(s):
    arr = 0
    for i in s:
        if i == "(":
            arr += 1
        else :
            arr -= 1
        if arr < 0:
            return False
    if arr == 0 :
        return True
    else:
        return False