def solution(n):
    answer_list = [1] * n
    answer_list[0] = 0
    for i in range(2, int(n**(1/2))+1):
        t = 2
        while t*i < n+1:
            answer_list[t*i-1] = 0
            t += 1
    return sum(answer_list)