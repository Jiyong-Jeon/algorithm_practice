from collections import Counter
def solution(k, tangerine):
    # setting
    c = Counter(tangerine)
    t_dict = dict(c.most_common())
    answer = 0
    num = 0
    # greed
    for t in t_dict.items():
        if num >= k:
            break
        else:
            num += t[1]
            answer += 1
    return answer