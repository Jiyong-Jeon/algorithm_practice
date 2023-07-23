from collections import deque
def solution(stones, k):
    queue = deque([])
    answer = float('inf')
    cnt = 0
    for i, stone in enumerate(stones):
        while queue and queue[-1][1] < stone:
            queue.pop()
        queue.append((i, stone))
        while queue and queue[0][0] <= i - k:
            queue.popleft()
        if i >= k-1:
            answer = min(answer, queue[0][1])
        else:
            cnt += 1
    return answer