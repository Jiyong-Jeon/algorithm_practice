def solution(x):
    x_temp = x
    l = []
    
    # split
    while x != 0: 
        l.append(x % 10)
        x //= 10
    
    # check
    if x_temp % sum(l)==0:
        return True
    else:
        return False