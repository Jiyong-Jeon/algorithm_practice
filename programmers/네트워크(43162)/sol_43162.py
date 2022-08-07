def check(num, visited, computers):
    visited[num] = True
    for i, com in enumerate(computers[num]):
        if com == 1 and not visited[i]:
            check(i, visited, computers)


def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            check(i, visited, computers)
            answer += 1
    return answer