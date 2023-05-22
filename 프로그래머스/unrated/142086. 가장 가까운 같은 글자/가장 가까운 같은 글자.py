def solution(s):
    answer = []
    count_dict = dict()
    for i, c in enumerate(s):
        if c in count_dict.keys():
            answer.append(i-count_dict[c])
            count_dict[c] = i
        else:
            answer.append(-1)
            count_dict[c] = i
    return answer