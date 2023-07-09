from itertools import combinations
def solution(clothes):
    cloth_dict = dict()
    for cloth in clothes:
        if not cloth[1] in cloth_dict.keys():
            cloth_dict[cloth[1]] = 1
        else:
            cloth_dict[cloth[1]] += 1
    item_num = list(cloth_dict.values())
    answer = 1
    for item in item_num:
        answer *= (item+1)
    return answer-1