from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    cache = deque([])
    for city in cities:
        temp = city.lower()
        if temp in cache: # hit
            answer += 1
            cache.remove(temp)
            cache.appendleft(temp)
        else: # miss
            answer += 5
            if len(cache) >= cacheSize: 
                cache.pop()
                cache.appendleft(temp)
            else:
                cache.appendleft(temp)
                
    return answer