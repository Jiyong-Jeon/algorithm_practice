def hanoi(n, start, target, mid):
    if n == 2:
        return [[start, mid], [start, target], [mid, target]]
    return hanoi(n-1, start, mid, target) + [[start, target]] + hanoi(n-1, mid, target, start)

def solution(n):
    if n == 1:
        return [[1, 3]]
    answer = hanoi(n, 1, 3, 2)
    return answer