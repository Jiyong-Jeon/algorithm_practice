from collections import Counter

def splitNcheck(arr):
    if len(arr) == 1:
        return arr
    # set new arr
    new_arr = [[], [], [] ,[]]
    t = int(len(arr) ** (1/2))
    for i in range(t):
        if i < t//2:
            new_arr[0] += arr[i*t: i*t + t//2]
            new_arr[1] += arr[i*t + t//2 : i*t + t]
        else:
            new_arr[2] += arr[i*t: i*t + t//2]
            new_arr[3] += arr[i*t + t//2 : i*t + t]
    for i in range(4):
        sum_temp = sum(new_arr[i])
        if sum_temp in [0, len(arr)//4]:
            new_arr[i] = [0] if sum_temp == 0 else [1]
    return splitNcheck(new_arr[0]) + splitNcheck(new_arr[1]) + splitNcheck(new_arr[2]) + splitNcheck(new_arr[3])
            
def solution(arr):
    answer = []
    arr = sum(arr, [])
    if sum(arr) in [0, len(arr)]:
        return [1, 0] if sum(arr) == 0 else [0, 1]
    ct = Counter(splitNcheck(arr))
    return [ct[0], ct[1]]