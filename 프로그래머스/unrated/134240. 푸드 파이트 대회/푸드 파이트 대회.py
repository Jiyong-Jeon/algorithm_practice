def solution(food):
    temp = ''
    for i, num in enumerate(food):
        if i == 0:
            continue
        temp += str(i) * (num // 2)
    return temp + '0' + ''.join(reversed(temp))