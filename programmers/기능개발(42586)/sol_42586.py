def solution(progresses, speeds):
    days = [(100 - progresses[i]) // speeds[i] if ((100 - progresses[i]) % speeds[i]) == 0 else ((100 - progresses[i]) // speeds[i])+1 for i in range(len(progresses))]
    days = list(reversed(days))
    top = days.pop()
    count = 1
    answer = []
    if days == []:
        answer.append(count)
    while days:
        temp = days.pop()
        if top >= temp:
            count += 1
        else:
            top = temp
            answer.append(count)
            count = 1
    answer.append(count)
    return answer