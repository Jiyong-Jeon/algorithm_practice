def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    while k != 0:
        stack.pop()
        k -= 1
    return ''.join(stack)

    # 시간 초과 코드
    # number = list(map(int, number))
    # for _ in range(k):
    #     temp = 10
    #     flag = True
    #     for num in number:
    #         if temp < num:
    #             number.remove(temp)
    #             flag = False
    #             break
    #         else:
    #             temp = num
    #     if flag:
    #         number.pop()
    # return ''.join(map(str, number))