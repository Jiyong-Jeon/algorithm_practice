def solution(code):
    mode = False # False : 0, True : 1
    answer = ''
    for i, c in enumerate(code):
        if c == '1':
            mode = not mode
        else:
            if (not mode) and (i % 2 ==0):
                answer += c
            elif (mode) and (i % 2 ==1):
                answer += c
    if answer == '':
        return "EMPTY"
    return answer