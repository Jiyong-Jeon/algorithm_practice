########
# 1차 시도 , 정확성통과 , 시간초과
# import numpy as np
# def solution(land):
#     for i in range(1, len(land)):
#         for j in range(4):
#             land[i][j] = max(np.array(land[i-1])[[k for k in range(4) if k != j]].tolist()) + land[i][j]
#     return max(land[-1])
##################
# 2차시도 통과
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            temp = land[i-1][j]
            land[i-1][j] = 0
            land[i][j] = max(land[i-1]) + land[i][j]
            land[i-1][j] = temp
    return max(land[-1])