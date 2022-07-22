import itertools
def prime_check(n):
    n_root = int(n ** (1/2))
    for i in range(2, n_root+1):
        if n % i == 0:
            return True
    return False
def solution(numbers):
    num_list = []
    for i in range(1, len(numbers)+1):
        temp = itertools.permutations(list(numbers), i)
        for j in temp:
            num = int(''.join(j))
            if num > 1:
                num_list.append(num)
    num_list = list(set(num_list))
    answer_list = [ num for num in num_list if not prime_check(num)]
    return len(answer_list)

print(solution('17'))