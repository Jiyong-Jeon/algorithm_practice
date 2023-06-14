def solution(p):
    def trans(s):
        if not s:
            return ''
        open_num = 0
        close_num = 0
        if s[0] == "(":
            open_num += 1
        else:
            close_num += 1
        i = 1
        while open_num != close_num and i < len(s):
            if s[i] == "(":
                open_num += 1
            else:
                close_num += 1
            i += 1
        u, v = s[:i], s[i:]
        if s[0] == '(':
            return ''.join(u) + ''.join(trans(v))
        else:
            temp = [')' if s == '(' else '(' for s in u[1:-1]]
            return '(' + ''.join(trans(v)) + ')' + ''.join(temp)
    return trans(list(p))