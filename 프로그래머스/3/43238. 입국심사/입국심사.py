def solution(n, times):
    def can_num(time):
        return sum([time//t for t in times])
    min_t = 1
    max_t = max(times) * n
    while True:
        mid_t = (min_t+max_t) // 2
        people_num = can_num(mid_t)
        if people_num >= n:
            max_t = mid_t
        else:
            min_t = mid_t
        if min_t == max_t-1:
            return max_t