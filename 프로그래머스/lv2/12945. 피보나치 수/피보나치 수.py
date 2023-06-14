def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    pre, cur = 0, 1
    for i in range(2, n+1):
        pre, cur = cur, pre+cur
    return cur % 1234567

# 시간초과
# def fi(n): 
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fi(n-1) + fi(n-2)