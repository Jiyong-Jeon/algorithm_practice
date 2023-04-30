def solution(d, budget):
    d.sort(reverse=True)
    answer = 0
    while d:
        m = d.pop()
        if m <= budget:
            budget -= m
            answer += 1
        else:
            break
    return answer