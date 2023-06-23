def solution(s):
    count = 0
    remove_num = 0
    while s != '1':
        count += 1
        remove_num += s.count('0')
        temp = [c for c in s if c=='1']
        s = bin(len(temp))[2:]
        
    return [count, remove_num]