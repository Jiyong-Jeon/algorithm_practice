def solution(a, b, n):
    temp = (n//a) * b
    save = n % a
    answer = temp
    while temp>0:
        k = temp + save
        temp = (k // a) * b
        save = k % a
        answer += temp
        
        
    return answer