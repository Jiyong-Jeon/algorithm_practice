def change_num(n, k, k_number):
    if n == 0:
        return '0'
    num = ''
    while n > 0:
        num += k_number[n % k]
        n //= k
    return ''.join(reversed(num))

def prime(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return 0
    return 1

def solution(n, k):
    k_number = [str(i) for i in range(k)]
    check_list = [prime(int(num)) for num in change_num(n, k, k_number).split('0') if num != '' and num != '1']
    return sum(check_list)