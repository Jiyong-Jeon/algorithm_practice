def solution(s, n):
    answer = ''
    for c in s:
        c_num = ord(c)
        if c_num >= 97 and c_num <= 122:
            temp = 97
        elif c_num >= 65 and c_num <= 90:
            temp = 65
        else:
            answer += ' '
            continue
        c_num = (c_num - temp + n) % 26
        answer += chr(c_num + temp)
    return answer