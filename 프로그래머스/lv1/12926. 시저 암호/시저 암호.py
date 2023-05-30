def solution(s, n):
    answer = ''
    for c in s:
        if c.islower():
            temp = ord("a")
        elif c.isupper():
            temp = ord("A")
        else:
            answer += ' '
            continue
        c_num = (ord(c) - temp + n) % 26
        answer += chr(c_num + temp)
    return answer