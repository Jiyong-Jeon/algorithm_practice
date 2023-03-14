x, y = map(int, input().split(" "))
u = (y * 100) // x
low = 0
high = 1000000000
if u >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high)//2
        temp = ((y+mid) * 100 ) // (x+mid)
        if temp <= u:
            low = mid+1
        else:
            answer = mid
            high = mid-1
    print(answer)
