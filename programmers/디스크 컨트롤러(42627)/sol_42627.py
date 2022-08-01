import heapq
from collections import deque
def solution(jobs):
    time = 0
    answer = 0
    d = len(jobs)
    jobs.sort(key=lambda x:x[0])
    heap = []
    jobs = deque(jobs)
    while True:
        while len(jobs) != 0:
            if jobs[0][0] > time:
                if heap == []:
                    time+=1
                else:
                    break
            else:
                temp = jobs.popleft()
                heapq.heappush(heap, (temp[1], temp[0]))
        temp = heapq.heappop(heap)
        answer += time + temp[0] - temp[1]
        time += temp[0]
        if len(jobs) == 0 and heap == []:
            return answer // d