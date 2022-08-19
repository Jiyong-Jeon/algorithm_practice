def solution(nums):
    n = len(nums) // 2
    if n <= len(set(nums)):
        return n
    else:
        return len(set(nums))