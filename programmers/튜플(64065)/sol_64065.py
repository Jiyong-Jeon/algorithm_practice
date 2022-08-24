def solution(s):
    temp = [ [k.split(',') for k in t.split('}') if k != ',' and k != ''] for t in s.split('{') if '}' in t ]
    temp = [ list(map(int, t[0])) for t in temp]
    temp.sort(key=lambda x:len(x))
    answer = []
    for tem in temp:
        for t in tem:
            if not t in answer:
                answer.append(t)
    return answer