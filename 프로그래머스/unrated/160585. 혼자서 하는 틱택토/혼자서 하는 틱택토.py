def game_check(board, mark):
    fin_cnt = 0
    lr_cross_cnt = 0
    rl_cross_cnt = 0
    for i in range(3):
        r_cnt, c_cnt = 0, 0
        for j in range(3):
            # row
            if board[i][j] == mark:
                r_cnt += 1
            # col
            if board[j][i] == mark:
                c_cnt += 1
        # cross
        if board[i][i] == mark:
            lr_cross_cnt += 1
        if board[i][2-i] == mark:
            rl_cross_cnt += 1
        if r_cnt == 3:
            fin_cnt += 1
        if c_cnt == 3:
            fin_cnt += 1
    if lr_cross_cnt == 3:
        fin_cnt += 1
    if rl_cross_cnt == 3:
        fin_cnt += 1
    return fin_cnt

def solution(board):
    o_cnt, x_cnt = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                o_cnt += 1
            elif c == 'X':
                x_cnt += 1
    if not o_cnt - x_cnt in [0, 1]:
        return 0
    o_fin, x_fin = game_check(board, 'O'), game_check(board, 'X')
    if o_fin > 2 or x_fin > 1 or (o_fin>0 and x_fin>0):
        return 0
    if (o_fin == 1 and o_cnt-x_cnt != 1) or (x_fin == 1 and o_cnt!=x_cnt):
        return 0
    return 1