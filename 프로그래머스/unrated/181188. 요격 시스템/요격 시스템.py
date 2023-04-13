def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[0],x[1]))
    e = -1
    for target in targets:
        if target[0] < e:
            if target[1] < e:
                e = target[1]
        else:
            s = target[0]
            e = target[1]
            answer += 1
    return answer