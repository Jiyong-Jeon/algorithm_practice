# 동적계획법
def check(n, temp, number, level):
    if temp > 32000 or temp <= 0:
        return 0
    if temp == number:
        level[n - 1].append(temp)
        return n
    if level != 1:
        c = True
        for i in range(n):
            if temp in level[i]:
                c = False
        if c:
            level[n - 1].append(temp)
    else:
        level[n-1].append(temp)
    return 0

def level_check(l, N, number, level):
    # N
    temp = N * int('1' * l)
    c = check(l, temp, number, level)
    if c != 0:
        return c
    # 사칙연산
    check_list = []
    for i in range(1, l): #make check list
        for j in range(1, l):
            if i + j == l:
                check_list.append((i-1, j-1))
    for pair in check_list:
        # +
        for p1 in level[pair[0]]:
            for p2 in level[pair[1]]:
                temp = p1 + p2
                c = check(l, temp, number, level)
                if c != 0:
                    return c
        # -
        for p1 in level[pair[0]]:
            for p2 in level[pair[1]]:
                temp = p1 - p2
                c = check(l, temp, number, level)
                if c != 0:
                    return c
        # *
        for p1 in level[pair[0]]:
            for p2 in level[pair[1]]:
                temp = p1 * p2
                c = check(l, temp, number, level)
                if c != 0:
                    return c
        # //
        for p1 in level[pair[0]]:
            for p2 in level[pair[1]]:
                if p1 % p2 != 0:
                    continue
                temp = p1 // p2
                c = check(l, temp, number, level)
                if c != 0:
                    return c
    return 0

def solution(N, number):
    level = [ [] for _ in range(8)]
    for i in range(8):
        if level_check(i+1, N, number, level) != 0:
            return i+1
    return -1