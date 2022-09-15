def solution(n):
    temp = int(n ** 0.5)
    if temp ** 2 == n:
        return (temp+1) ** 2
    else:
        return -1

# 다른 사람풀이
# temp = n ** 0.5
# if temp % 1 == 0: # 정수인지 판별