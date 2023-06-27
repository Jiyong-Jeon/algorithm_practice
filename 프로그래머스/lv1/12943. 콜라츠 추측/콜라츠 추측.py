def solution(num):
    if num == 1:
        return 0
    answer = 0
    while answer <= 500:
        answer += 1
        num = (num // 2) if num % 2 ==0 else (num * 3 + 1)
        if num == 1:
            return answer
    return -1