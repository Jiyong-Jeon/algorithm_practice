def solution(dartResult):
    answer = []
    i = 0
    while i < len(dartResult):
        if dartResult[i] == '*':
            if len(answer) == 1:
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
        elif dartResult[i] == '#':
            answer[-1] = -answer[-1]
        else:
            temp = int(dartResult[i])
            if temp == 1 and dartResult[i + 1] == '0':
                temp = 10
                i += 1
            if dartResult[i + 1] == 'S':
                answer.append(temp)
            elif dartResult[i + 1] == 'D':
                answer.append(temp ** 2)
            elif dartResult[i + 1] == 'T':
                answer.append(temp ** 3)
            i += 1
        i += 1
    print(answer)

    return sum(answer)