from collections import deque
def solution(operations):
    dq = deque()
    for op in operations:
        order = op.split(" ")
        if order[0] == "I":
            temp = int(order[1])
            if len(dq) == 0:
                dq.append(temp)
            else:
                for i in range(len(dq)):
                    if temp <= dq[i]:
                        dq.insert(i, temp)
                        break
                    if i == len(dq) -1:
                        dq.append(temp)
        else:
            if len(dq) == 0:
                continue
            if order[1] == '1':
                dq.pop()
            else:
                dq.popleft()
    if len(dq) == 0:
        return [0, 0]
    else:
        return [dq[-1], dq[0]]