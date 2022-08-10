from collections import deque
def solution(people, limit):
    people.sort()
    people_q = deque(people)
    answer = 0
    while people_q:
        p = people_q.popleft()
        answer += 1
        if p > limit:
            return answer + len(people_q)
        else:
            while people_q:
                p2 = people_q.pop()
                if (limit - p2) < p:
                    answer += 1
                    continue
                else:
                    break
    return answer