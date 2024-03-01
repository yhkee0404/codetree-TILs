with open(0) as f:
    n = int(f.readline().strip())
    points = sorted(tuple(map(int, line.split())) for line in f.readlines())

def d(a, b):
    return sum(map(lambda x: x * x, (a[i] - b[i] for i in range(len(a)))))

adj = [[None] * n for _ in range(n)]
for i in range(n):
    ai = adj[i]
    pi = points[i]
    for j in range(i + 1, n):
        ai[j] = d(pi, points[j])

MAX_DP = 1_000_000_000_000_000_000
dp = [[MAX_DP] * n for _ in range(n)]
dp[0][0] = 0
for i in range(n - 1):
    for j in range(n - 1):
        if dp[i][j] == MAX_DP:
            continue
        dij = dp[i][j]
        k = max(i, j) + 1
        dp[i][k] = min(dp[i][k], dij + adj[j][k])
        dp[k][j] = min(dp[k][j], dij + adj[i][k])
dp[-1][-1] = adj[-1][-1] = 0
print(min(dp[i][-1] + adj[i][-1] for i in range(n - 1)))