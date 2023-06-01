# import itertools
# answer = list(itertools.permutations(range(1, n+1), n))[k-1]
# 시간초과
def solution(n, k):
    answer = []
    num_list = list(range(1, n+1))
    div_num = 1
    
    # factorial : !(n-1)
    for i in range(1, n):
        div_num *= i
        
    for i in range(n, 0, -1):
        q = k // div_num
        r = k % div_num
        if r == 1:
            answer.append(num_list.pop(q))
            answer += num_list
            break
        elif r == 0:
            answer.append(num_list.pop(q-1))
            k = div_num
        else:
            answer.append(num_list.pop(q))
            k = r
        if i == 1:
            answer += num_list
            break
        div_num //= (i-1)
            
    return answer 