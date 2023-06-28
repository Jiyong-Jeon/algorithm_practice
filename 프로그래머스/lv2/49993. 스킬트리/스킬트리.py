def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        pre = -1
        p = True
        for c in skill:
            if c in skill_tree:
                if pre == -2:
                    p = False
                    break
                temp = skill_tree.index(c)
                if pre < temp:
                    pre = temp
                else:
                    p = False
                    break
            else:
                pre = -2
        if p:
            answer += 1
    return answer