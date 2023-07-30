def num2n(num, n):
    if num == 0:
        return '0'
    return_str = []
    while num != 0:
        temp = num % n
        if temp >= 10:
            temp -= 10
            temp = chr(ord('A')+temp)
        return_str.append(str(temp))
        num //= n
    return ''.join(reversed(return_str))

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    turn = 0
    while len(answer) < t:
        number_str = num2n(cnt, n)
        for c in number_str:
            if turn == p-1:
                answer += c
                if len(answer) == t:
                    break
            turn = (turn + 1) % m
        cnt += 1
    return answer