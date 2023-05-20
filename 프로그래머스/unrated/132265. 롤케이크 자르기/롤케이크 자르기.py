from collections import Counter
def solution(topping):
    answer = 0
    c = Counter(topping)
    b = set()
    for t in topping:
        c[t] -= 1
        if c[t] == 0:
            del c[t]
        b.add(t)
        if len(c) == len(b):
            answer += 1
    return answer