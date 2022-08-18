from collections import deque
def solution(queue1, queue2):
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    sum_num = sum_1 + sum_2
    half_num = sum_num // 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    while True:
        if answer > (len(queue1) + len(queue2) + 2):
            return -1
        if sum_1 == half_num or sum_2 == half_num:
            return answer
        if sum_1 > half_num:
            temp = []
            while sum_1 > half_num:
                n = queue1.popleft()
                temp.append(n)
                sum_1 -= n
                sum_2 += n
                answer += 1
            queue2 += temp
        elif sum_2 > half_num:
            temp = []
            while sum_2 > half_num:
                n = queue2.popleft()
                temp.append(n)
                sum_2 -= n
                sum_1 += n
                answer += 1
            queue1 += temp
