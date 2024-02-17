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
    visit ^= True
    for v in adj[src]:
        if visited[v]:
            continue
        ans += dfs(adj, visited, v, visit)
    visited[src] = False
    return ans

visited = [False] * (n + 1)
print(min(dfs(adj, visited, 1, visit) for visit in (True, False)))