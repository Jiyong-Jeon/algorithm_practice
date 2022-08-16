import numpy as np
def rotation(map,r1,c1,r2,c2):
    min_num = 1000000
    temp = map[r1][c2]
    min_num = min(min_num, temp)
    for i in range(c2, c1, -1): # 우
        min_num = min(min_num, map[r1][i])
        map[r1][i] = map[r1][i-1]
    temp2 = map[r2][c2]
    min_num = min(min_num, temp2)
    for i in range(r2, r1, -1): # 하
        min_num = min(min_num, map[i][c2])
        map[i][c2] = map[i-1][c2]
    map[r1+1][c2] = temp
    temp = map[r2][c1]
    min_num = min(min_num, temp)
    for i in range(c1, c2): # 좌
        min_num = min(min_num, map[r2][i])
        map[r2][i] = map[r2][i+1]
    map[r2][c2-1] = temp2
    for i in range(r1, r2): # 상
        min_num = min(min_num, map[i][c1])
        map[i][c1] = map[i+1][c1]
    map[r2-1][c1] = temp
    return min_num

def solution(rows, columns, queries):
    map = np.arange(1, rows*columns+1).reshape(rows, columns).tolist()
    answer = []
    for q in queries:
        answer.append(rotation(map, q[0]-1, q[1]-1, q[2]-1, q[3]-1))
        print(map)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))