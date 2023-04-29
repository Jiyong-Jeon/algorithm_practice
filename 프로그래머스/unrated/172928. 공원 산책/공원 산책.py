def check(cur_pos, cmd, park):
    direction, distance = cmd.split(" ")
    if direction == 'E':
        if cur_pos[1]+int(distance) < len(park[0]):
            for i in range(cur_pos[1], cur_pos[1]+int(distance)+1):
                if park[cur_pos[0]][i] == "X":
                    return cur_pos
            return [cur_pos[0], cur_pos[1]+int(distance)]
    if direction == 'W':
        if cur_pos[1]-int(distance) > -1:
            for i in range(cur_pos[1]-int(distance), cur_pos[1]):
                if park[cur_pos[0]][i] == "X":
                    return cur_pos
            return [cur_pos[0], cur_pos[1]-int(distance)]
    if direction == 'S':
        if cur_pos[0]+int(distance) < len(park):
            for i in range(cur_pos[0], cur_pos[0]+int(distance)+1):
                if park[i][cur_pos[1]] == "X":
                    return cur_pos
            return [cur_pos[0]+int(distance), cur_pos[1]]
    if direction == 'N':
        if cur_pos[0]-int(distance) > -1:
            for i in range(cur_pos[0]-int(distance), cur_pos[0]):
                if park[i][cur_pos[1]] == "X":
                    return cur_pos
            return [cur_pos[0]-int(distance), cur_pos[1]]
    return cur_pos
    
def solution(park, routes):
    pos = [[i,j] for i in range(len(park)) for j in range(len(park[0])) if park[i][j] == 'S'][0]
    park = [list(p) for p in park]
    for route in routes:
        pos = check(pos, route, park)
    return pos