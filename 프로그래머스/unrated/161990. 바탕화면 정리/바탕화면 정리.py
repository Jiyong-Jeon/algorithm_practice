def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 1000, 1000, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if i + 1 > rdx:
                    rdx = i+1
                if j < luy:
                    luy = j
                if j+1 > rdy:
                    rdy = j+1
    return [lux, luy, rdx, rdy]