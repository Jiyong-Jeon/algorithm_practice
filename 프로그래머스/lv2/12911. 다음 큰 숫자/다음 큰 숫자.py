def solution(n):
    n_count = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == n_count:
            return (n)