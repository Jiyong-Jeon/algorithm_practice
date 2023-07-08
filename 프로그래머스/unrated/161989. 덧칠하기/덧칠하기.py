def solution(n, m, section):
    answer = 1
    section.sort(reverse=True)
    end = section.pop() + m - 1
    while section:
        s = section.pop()
        if s > end:
            answer += 1
            end = s + m - 1
        
    return answer