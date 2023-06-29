def move(cur_pos, d):
    if d == 'U':
        reversed_d = 'D'
        if cur_pos[1] + 1 < 6:
            return [cur_pos[0], cur_pos[1]+1], reversed_d
    elif d == 'D':
        reversed_d = 'U'
        if cur_pos[1] - 1 > -6:
            return [cur_pos[0], cur_pos[1]-1], reversed_d
    elif d == 'R':
        reversed_d = 'L'
        if cur_pos[0] + 1 < 6:
            return [cur_pos[0]+1, cur_pos[1]], reversed_d
    else: # 'L'
        reversed_d = 'R'
        if cur_pos[0] - 1 > -6:
            return [cur_pos[0]-1, cur_pos[1]], reversed_d
    return cur_pos, None
        
def solution(dirs):
    answer = 0
    cur_pos = [0, 0]
    visited = []
    for d in dirs:
        temp_pos, reversed_d = move(cur_pos, d)
        temp_pos.append(d)
        if (reversed_d != None) and (not temp_pos in visited):
            answer += 1
            cur_pos.append(reversed_d)
            
            visited.append(temp_pos)
            visited.append(cur_pos)
            
        cur_pos = [temp_pos[0], temp_pos[1]]
    return answer