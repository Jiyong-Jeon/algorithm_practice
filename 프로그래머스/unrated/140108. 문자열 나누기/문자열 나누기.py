def solution(s):
    answer = 0
    x = None
    x_count = 0
    non_count = 0
    for c in s:
        if x == None:
            x = c
            x_count = 1
        else:
            if x == c:
                x_count += 1
            else:
                non_count += 1
        if x_count == non_count:
            answer += 1
            x = None
            x_count = 0
            non_count = 0
    return answer +1 if x != None else answer