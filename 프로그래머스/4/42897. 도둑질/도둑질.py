def solution(money):
    dp1 = [money[0],money[1]]
    dp2 = [money[1],money[2]]
    for i in range(2, len(money)-1):
        dp1[i-1] = max(dp1[i-1], dp1[i-2])
        dp2[i-1] = max(dp2[i-1], dp2[i-2])
        dp1.append(max(dp1[i-2]+money[i], dp1[i-1]))
        dp2.append(max(dp2[i-2]+money[i+1], dp2[i-1]))
    return max(dp1[-1], dp2[-1])