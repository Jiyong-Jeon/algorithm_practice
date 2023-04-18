def solution(t, p):
    answer = 0
    for s_i in range(len(t)-len(p)+1):
        if int(t[s_i:s_i+len(p)]) <= int(p):
            answer += 1
    return answer