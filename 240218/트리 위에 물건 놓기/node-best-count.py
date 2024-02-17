with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, f.readline().split())
        adj[u].append(v)
        adj[v].append(u)

import sys
sys.setrecursionlimit(n + 10)

def dfs(n, adj, dp, u, v, visit):
    ans = dp[v][visit]
    if ans != n:
        return ans
    ans = visit
    for w in adj[v]:
        if w == u:
            continue
        a = dfs(n, adj, dp, v, w, 1)
        if visit:
            b = dfs(n, adj, dp, v, w, 0)
            a = min(a, b)
        ans += a
    dp[v][visit] = ans
    return ans

dp = [[n] * 2 for _ in range(n + 1)]
adj[0].append(1)
print(dfs(n, adj, dp, -1, 0, 1) - 1)