import itertools
def check_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for num in itertools.combinations(nums, 3):
        if check_prime(sum(num)):
            answer += 1
    return answer