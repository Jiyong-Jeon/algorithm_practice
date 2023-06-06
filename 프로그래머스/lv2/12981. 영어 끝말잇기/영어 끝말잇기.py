def solution(n, words):
    answer = [0 ,0]
    stack = []
    for i, word in enumerate(words):
        if i % n == 0:
            answer[1] += 1
        if stack == []:
            stack.append(word)
            continue
        if stack[-1][-1] != word[0] or word in stack:
            answer[0] = (i % n) + 1
            return answer
        stack.append(word)

    return [0, 0]