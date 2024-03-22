def solution(k, ranges):
    cur_k = k
    area_list = []
    while cur_k != 1:
        if cur_k % 2 != 0:
            area_list.append(cur_k +(((cur_k*3+1) - cur_k) / 2))
            cur_k = cur_k*3+1
        else:
            area_list.append(cur_k/2 + cur_k/4)
            cur_k /= 2
    answer = []
    for r in ranges:
        a = r[0]
        b = len(area_list)+r[1]
        if r == [0, 0]:
            answer.append(sum(area_list))
            continue
        if a > b:
            answer.append(-1.0)
            continue
        answer.append(sum(area_list[a:b]))
    return answer