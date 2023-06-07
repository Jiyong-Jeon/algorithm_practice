from itertools import combinations
def solution(relation):
    answer_list = []
    attribute = [i for i in range(len(relation[0]))]
    for i in range(len(relation[0])):
        for com in combinations(attribute, i+1):
            if len(relation) == len(set([tuple([r[a] for a in com]) for r in relation])):
                can_answer = True
                for answer in answer_list:
                    if len(set(answer+com)) == len(com):
                        can_answer = False
                        break
                if can_answer:
                    answer_list.append(com)
    return len(answer_list)