def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n = n//2
        else:
            n -= 1
            ans += 1
    return ans

# dp 방식 시간초과 ( 10억 **)
# def solution(n):
#     dp = [0] * (n+1)
#     dp[1] = 1
#     for i in range(2, n+1):
#         if i % 2 == 0:
#             dp[i] = min(dp[i-1]+1, dp[i//2])
#         else:
#             dp[i] = dp[i-1] + 1
#     return dp[-1]