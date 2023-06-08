from heapq import heappush, heapify, heappop
def solution(n, k, enemy):
    heap = enemy[:k]
    answer = len(heap)
    heapify(heap)
    for i in range(k, len(enemy)):
        heappush(heap, enemy[i])
        answer += 1
        if heap[0] > n:
            answer -= 1
            break
        else:
            n -= heappop(heap)
    return answer