
def solution(n, arr1, arr2):
    map1 = [list('0'*(n-len(str(bin(a))[2:]))+str(bin(a))[2:]) for a in arr1 ]
    map2 = [list('0'*(n-len(str(bin(a))[2:]))+str(bin(a))[2:]) for a in arr2 ]
    return [ ''.join(['#' if map1[i][j] == '1' or map2[i][j] == '1' else ' ' for j in range(n)]) for i in range(n)]