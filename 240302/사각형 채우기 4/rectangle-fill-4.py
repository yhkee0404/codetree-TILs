with open(0) as f:
    n = int(f.read().strip())

m = 10_007

dp = [[0] * (1 << 3) for _ in range(n + 2)]
dp[0][0] = 1
for i in range(n):
    u = dp[i]
    v = u[0]
    dp[i + 2][0] = (dp[i + 2][0] + v) % m
    dp[i + 1][1] = (dp[i + 1][1] + v) % m
    dp[i + 1][4] = (dp[i + 1][4] + v) % m
    v = u[1]
    dp[i + 1][0] = (dp[i + 1][0] + v) % m
    dp[i + 1][6] = (dp[i + 1][6] + v) % m
    v = u[3]
    dp[i + 1][4] = (dp[i + 1][4] + v) % m
    v = u[4]
    dp[i + 1][0] = (dp[i + 1][0] + v) % m
    dp[i + 1][3] = (dp[i + 1][3] + v) % m
    v = u[6]
    dp[i + 1][1] = (dp[i + 1][1] + v) % m
    
print(dp[n][0])