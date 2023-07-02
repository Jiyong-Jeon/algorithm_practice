def solution(book_time):
    # setting
    answer = 0
    in_time = []
    out_time = []
    for time in book_time:
        # in 
        h, m = map(int, time[0].split(":"))
        in_time.append(h*60 + m)
        # out
        h, m = map(int, time[1].split(":"))
        out_time.append(h*60 + m + 10)
    in_time.sort(reverse=True)
    out_time.sort(reverse=True)
    
    count = 0
    while in_time:
        if in_time[-1] >= out_time[-1]:
            count -= 1
            out_time.pop()
        else:
            count += 1
            in_time.pop()
        
        if count > answer:
            answer = count
    
    return answer