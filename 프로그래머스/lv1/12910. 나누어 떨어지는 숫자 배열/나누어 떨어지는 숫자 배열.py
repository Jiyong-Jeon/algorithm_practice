def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if answer == []:
        return [-1]
    else:
        return sorted(answer)