with open(0) as f:
    n = int(f.readline().strip())
    a = tuple(tuple(map(int, line.split())) for line in f.readlines())

def visit(n, a, visited, k, dp):
    if visited + 1 == 1 << n:
        return a[k][0]
    if dp[visited][k] is not None:
        return dp[visited][k]
    bit = 1
    ans = 1_000_000
    for i in range(n):
        if a[k][i] and not (visited & bit):
            ans = min(ans, visit(n, a, visited | bit, i, dp) + a[k][i])
        bit <<= 1
    dp[visited][k] = ans
    return ans

dp = [[None] * n for _ in range(1 << n)]
print(visit(n, a, 1, 0, dp))