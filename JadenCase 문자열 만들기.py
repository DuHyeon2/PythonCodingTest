def solution(s):
    answer = ''
    arr = s.split(' ')

    for i in range(len(arr)):
        arr[i]=arr[i].capitalize()
    answer = ' '.join(arr)

    return answer