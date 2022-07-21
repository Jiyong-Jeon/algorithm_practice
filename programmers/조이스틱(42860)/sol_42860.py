def check_c(c):
    dif = (ord(c) - ord('A'))
    if dif > 13:
        dif = 13 - dif % 13
    return dif

def return_d(tf_list, num_list):
    temp = [ len(num_list) - i if i > (len(num_list)//2) else i for i in range(len(num_list))]
    d = []
    for i in range(len(num_list)):
        d.append(temp.copy())
        temp.insert(0, temp.pop())
    for idx, t in enumerate(d):
        if idx in tf_list or idx == 0:
            for i, te in enumerate(t):
                if not i in tf_list:
                    d[idx][i] = 0
        else:
            d[idx] = []
    return d

def backtracking(li, cur_idx, cur_score, d): #backtracking
    global best
    if li == []:
        if cur_score < best:
            best = cur_score
    else:
        for i, l in enumerate(li):
            temp = cur_score + d[cur_idx][l]
            if temp < best:
                list_temp = li.copy()
                list_temp.pop(i)
                backtracking(list_temp, l, temp, d)
best = 100000
def solution(name):
    global best
    name_num = [check_c(n) for n in name]
    tf_list = [ i for i, n in enumerate(name_num) if n > 0]
    d = return_d(tf_list, name_num)
    backtracking(tf_list, 0, 0, d)
    return best + sum(name_num) #greedy