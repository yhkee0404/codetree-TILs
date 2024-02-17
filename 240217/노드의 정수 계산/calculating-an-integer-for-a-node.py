with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        t, a, p = map(int, f.readline().split())
        adj[p].append((i, a if t else - a))

import sys
sys.setrecursionlimit(n + 10)

def dfs(adj, src):
    ans = 0
    for u, a in adj[src]:
        a += dfs(adj, u)
        ans += max(0, a)
    return ans

print(dfs(adj, 1))