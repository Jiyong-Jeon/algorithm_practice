def solution(k, d):
    answer = 0
    for i in range(int(d/k)+1):
        answer += int(((d**2) - (i*k)**2) ** (1/2)/k) + 1
    return answer