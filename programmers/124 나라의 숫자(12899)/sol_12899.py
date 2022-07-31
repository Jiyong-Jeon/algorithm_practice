def list_update(list, index):
    list[index-1] -= 1
    list[index] = 3
    if index-1 != 0 and list[index - 1] == 0:
        list_update(list, index - 1)

def solution(n):
    num = int(n)
    p = 0
    temp = 3 ** p
    pow_3 = [temp]
    p += 1
    temp = 3 ** p
    while temp <= num:
        pow_3.append(temp)
        p += 1
        temp = 3 ** (p)
    answer = []
    for i in reversed(pow_3):
        temp = num // i
        if temp == 0:
            answer.append(3)
            list_update(answer, len(answer) - 1)
            num = num % i
        else:
            answer.append(temp)
            num = num % i
    answer = [4 if a == 3 else a for a in answer]
    if answer[0] == 0:
        del answer[0]

    return ''.join(map(str, answer))

print(solution('3'))


############ 깔끔 해답
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

