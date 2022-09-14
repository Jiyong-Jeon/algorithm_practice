def solution(n, lost, reserve):
    l = 0
    lost.sort()
    reserve.sort()
    lost1 = list(set(lost) - set(reserve))
    reserve1 = list(set(reserve) - set(lost))

    for i in lost1:
        if i in reserve1:
            reserve1.pop(reserve1.index(i))
        elif i - 1 in reserve1:
            reserve1.pop(reserve1.index(i - 1))
        elif i + 1 in reserve1:
            reserve1.pop(reserve1.index(i + 1))
        else:
            l += 1

    return n - l