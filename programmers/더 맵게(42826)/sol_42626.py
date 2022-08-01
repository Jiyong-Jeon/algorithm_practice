# 첫 시도 (정확도 성공, 효율성에서 실패)
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if scoville[0] >= K:
            return answer
        else:
            if len(scoville) >= 2:
                one = scoville.pop(0)
                two = scoville.pop(0)
                temp = one + (two * 2)
                answer += 1
                if len(scoville) == 0:
                    scoville.append(temp)
                else:
                    for i in range(len(scoville)):
                        if scoville[i] >= temp:
                            scoville.insert(i, temp)
                            break
                        if len(scoville)-1 == i:
                            scoville.append(temp)
            else:
                return -1

############################
# 두번째 heapq 사용 성공
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        else:
            if len(scoville) >= 2:
                one = heapq.heappop(scoville)
                two = heapq.heappop(scoville)
                temp = one + (two * 2)
                answer += 1
                heapq.heappush(scoville, temp)
            else:
                return -1