from collections import defaultdict, deque
def solution(n, edge):
    # setting
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # BFS
    check_dis = [-1] * n
    check_dis[0] = 0
    check_list = deque([1])
    while check_list:
        cur_n = check_list.popleft()
        cur_dis = check_dis[cur_n-1]
        for check_n in graph[cur_n]:
            if check_dis[check_n-1] == -1:
                check_dis[check_n-1] = cur_dis + 1
                check_list.append(check_n)
    return check_dis.count(max(check_dis))