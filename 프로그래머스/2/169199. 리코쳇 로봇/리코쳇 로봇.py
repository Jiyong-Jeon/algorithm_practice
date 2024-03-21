from collections import deque
def solution(board):
    def check_can_move(cur_pos, board, count):
        # 상하좌우
        d_x = [0, 0, -1, 1]
        d_y = [-1, 1, 0, 0]
        board[cur_pos[1]][cur_pos[0]] = 'X'
        move = []
        for i in range(4): #상하좌우 체크
            x, y = cur_pos
            while True:
                x += d_x[i]
                y += d_y[i]
                if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board): # 라인 아웃
                    break
                elif board[y][x] == "D": # 벽
                    break
            x -= d_x[i]
            y -= d_y[i]
            if board[y][x] != 'X':
                move.append([(x, y), count+1])
        return move

    # set init
    board = [list(s) for s in board]
    cur_pos = (-1, -1)
    check_g = False
    for y, s in enumerate(board):
        for x, c in enumerate(s):
            if c == 'R':
                cur_pos = (x, y)
            if c == 'G': # 골인 지점이 가능한지 확인
                if (x-1) < 0 or (x+1) >= len(s) or (y-1) < 0 or (y+1) >= len(board): 
                    check_g = True
                elif board[y][x-1] == "D" or board[y][x+1] == "D" or board[y-1][x] == "D" or board[y+1][x] == "D":
                    check_g = True
                else:
                    return -1
            if check_g and cur_pos != (-1, -1):
                break
    move_list = deque(check_can_move(cur_pos, board, 0)) # init
    while move_list:
        move = move_list.popleft()
        x, y = move[0]
        count = move[1]
        if board[y][x] == "G": # goal
            return count
        move_list.extend(check_can_move((x, y), board, count))
    return -1