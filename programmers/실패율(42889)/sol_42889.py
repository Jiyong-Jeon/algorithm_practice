import numpy as np
from collections import Counter
def solution(N, stages):
    stages = np.array(stages)
    l = []
    t = Counter(stages)
    for i in range(1, N+1):
        c = Counter(stages>=i)[True]
        if c == 0:
            if Counter(stages)[i] != 0:
                l.append([i, 1])
            else:
                l.append([i, 0])
        else:
            l.append([i, t[i]/c])
    l.sort(key=lambda x:x[1], reverse = True)
    answer = [ temp[0] for temp in l ]
    return answer