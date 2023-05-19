from collections import Counter
def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)
    for i in range(9, -1, -1):
        answer += str(i) * min(x[str(i)], y[str(i)])
    if answer == '':
        return '-1'
    if answer[0]=='0' and len(answer)>1:
        return '0'
    return answer