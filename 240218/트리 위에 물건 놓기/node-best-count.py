with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, f.readline().split())
        adj[u].append(v)
        adj[v].append(u)

import sys
sys.setrecursionlimit(n + 10)

def dfs(adj, visited, src, visit):
    visited[src] = True
    if visit:
        ans = 1
    else:
        ans = 0
    for v in adj[src]:
        if visited[v]:
            continue
        a = dfs(adj, visited, v, True)
        if visit:
            b = dfs(adj, visited, v, False)
            a = min(a, b)
        ans += a
    visited[src] = False
    return ans

visited = [False] * (n + 1)
adj[0].append(1)
print(dfs(adj, visited, 0, True) - 1)