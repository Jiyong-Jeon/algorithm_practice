def solution(numbers):
    check = [numbers.pop()]
    answer = [-1]
    while numbers:
        num = numbers.pop()
        while check:
            c = check.pop()
            if num < c:
                answer.append(c)
                check.append(c)
                check.append(num)
                break
        if check==[]:
            answer.append(-1)
            check = [num]
    answer.reverse()
    return answer