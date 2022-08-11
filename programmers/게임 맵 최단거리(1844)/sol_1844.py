# DFS 활용 ( 가지치기 O ) 정확성 성공, 시간초과
# import copy
# def can_move(maps, loc):
#     # 동(0,1) 서(0,-1) 남(1,0) 북(-1,0)
#     move = []
#     if not loc[1] + 1 >= len(maps[0]):  # 동
#         if maps[loc[0]][loc[1] + 1] == 1:
#             move.append([loc[0], loc[1] + 1])
#     if not loc[0] + 1 >= len(maps):  # 남
#         if maps[loc[0] + 1][loc[1]] == 1:
#             move.append([loc[0] + 1, loc[1]])
#     if not (loc[1] - 1 < 0):
#         if (maps[loc[0]][loc[1] - 1] == 1):  # 서
#             move.append([loc[0], loc[1] - 1])
#     if not (loc[0] - 1 < 0):
#         if (maps[loc[0] - 1][loc[1]] == 1):  # 북
#             move.append([loc[0] - 1, loc[1]])
#     return move
#
# best = 1000000
# def search(maps, loc, count): # dfs
#     global best
#     maps[loc[0]][loc[1]] = 0
#     if loc[0] == len(maps) - 1 and loc[1] == len(maps[0]) - 1:
#         best = count
#         return
#     moves = can_move(maps, loc)
#     if moves == []:
#         return
#     for move in moves:
#         m = copy.deepcopy(maps)
#         if count + 1 >= best:
#             return
#         search(m, move, count + 1)
#
# def solution(maps):
#     global best
#     search(maps, [0, 0], 1)  # start dfs
#     return -1 if best == 1000000 else best

#########################
# bfs 활용  | 효율성, 정확성 통과
from collections import deque
def can_move(maps, loc, depth):
    # 동(0,1) 서(0,-1) 남(1,0) 북(-1,0)
    move = []
    if not loc[1] + 1 >= len(maps[0]):  # 동
        if maps[loc[0]][loc[1] + 1] == 1:
            move.append([loc[0], loc[1] + 1, depth])
    if not loc[0] + 1 >= len(maps):  # 남
        if maps[loc[0] + 1][loc[1]] == 1:
            move.append([loc[0] + 1, loc[1], depth])
    if not (loc[1] - 1 < 0):
        if (maps[loc[0]][loc[1] - 1] == 1):  # 서
            move.append([loc[0], loc[1] - 1, depth])
    if not (loc[0] - 1 < 0):
        if (maps[loc[0] - 1][loc[1]] == 1):  # 북
            move.append([loc[0] - 1, loc[1], depth])
    return move

def search(maps, loc, depth, queue):
    maps[loc[0]][loc[1]] = 0
    if loc[0] == len(maps) - 1 and loc[1] == len(maps[0]) - 1:
        return depth
    moves = can_move(maps, loc, depth + 1)
    if moves != []:
        queue += moves
    return 0

def solution(maps):
    queue = deque([[0, 0, 1]])
    while queue:
        temp = queue.popleft()
        if maps[temp[0]][temp[1]] == 0:
            continue
        answer = search(maps, [temp[0], temp[1]], temp[2], queue)
        if answer != 0:
            break
    return -1 if answer == 0 else answer