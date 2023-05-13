def solution(l, r):
    answer = []
    i = 1 
    while True:
        temp = int(bin(i)[2:])
        if temp >= 1000000:
            break
        if (temp * 5 >= l) and (temp*5 <= r):
            answer.append(temp*5)
        elif temp*5 > r:
            break
        i+=1
    if answer == []:
        return [-1]
    return answer