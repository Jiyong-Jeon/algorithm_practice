def solution(arr):
    answer = []
    temp = -1
    for a in arr:
        if a != temp:
            temp = a
            answer.append(temp)
    return answer