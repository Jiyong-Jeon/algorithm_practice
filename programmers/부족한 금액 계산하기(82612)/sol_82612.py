def solution(price, money, count):
    m = 0
    for c in range(1, count+1):
        m += price * c
    return 0 if money >= m else m-money