def solution(x):
    answer = True
    my_x = list(map(int, str(x)))
    arr = 0
    for i in my_x:
        arr += i

    if x % arr == 0:
        return True
    else:
        return False