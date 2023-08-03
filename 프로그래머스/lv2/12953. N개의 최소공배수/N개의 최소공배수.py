def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer