def solution(storey):
    best = 1000
    def dfs(num, cur_cost):
        nonlocal best
        check = num % 10
        next_num = num // 10
        if check <= 3:
            temp_cost = cur_cost + check
            if next_num == 0:
                if best > temp_cost:
                    best = temp_cost
            else:
                if temp_cost < best:
                    dfs(next_num, temp_cost)
        else:
            # non
            temp_cost = cur_cost + check
            if next_num == 0:
                if best > temp_cost:
                    best = temp_cost
            else:
                if temp_cost < best:
                    dfs(next_num, temp_cost)
            # up
            temp_cost = cur_cost + (10 - check)
            next_num += 1
            if temp_cost < best:
                dfs(next_num, temp_cost)
            
    dfs(storey, 0)
    return best