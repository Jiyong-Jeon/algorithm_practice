answer = 0
def search(num, numbers, target, depth):
    global answer
    if depth == len(numbers):
        if target == num:
            answer += 1
    else:
        search(num + numbers[depth], numbers, target, depth+1)
        search(num - numbers[depth], numbers, target, depth+1)

def solution(numbers, target):
    global answer
    search(0, numbers, target, 0)
    return answer