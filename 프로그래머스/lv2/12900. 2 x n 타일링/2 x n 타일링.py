def solution(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    return dp[-1] % 1000000007

# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8
