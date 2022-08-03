from collections import deque
def check(s):
    stack = []
    while s:
        temp = s.pop()
        if temp == ')' or temp == '}' or temp == ']':
            stack.append(temp)
        else:
            if stack == []:
                return False
            if not ((temp == '{' and stack[-1] == '}') or (temp == '(' and stack[-1] == ')') or (
                    temp == '[' and stack[-1] == ']')):
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False

def solution(s):
    st = deque(s)
    answer = 0
    for _ in range(len(st)):
        # print(st)
        if check(st.copy()):
            answer += 1
        st.append(st.popleft())

    return answer