def solution(n):
    i = 1
    while n % i != 1:
        i += 1
    return i