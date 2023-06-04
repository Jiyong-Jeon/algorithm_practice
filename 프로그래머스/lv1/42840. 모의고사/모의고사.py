def solution(answers):
    answer = [0, 0, 0]
    hater_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i, ans in enumerate(answers):
        for j, hater_ans in enumerate(hater_list):
            if ans == hater_ans[i%len(hater_ans)]:
                answer[j] += 1
    max_num = max(answer)
    return [i+1 for i, a in enumerate(answer) if a == max_num]