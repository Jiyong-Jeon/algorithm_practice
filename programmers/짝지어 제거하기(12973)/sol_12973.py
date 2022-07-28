# 효율성 문제 때문에 stack구조를 index만 활용하여 해결
def solution(s):
    s_list = list(s)
    check = [0]
    i = 1
    while i < len(s_list):
        if check:
            if s_list[check[-1]] == s_list[i]:
                del check[-1]
            else:
                check.append(i)
        else:
            check.append(i)
        i += 1
    if check:
        return 0
    else:
        return 1

print(solution('a'*100000))