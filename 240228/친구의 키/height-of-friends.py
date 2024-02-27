with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, f.readline().split())
        adj[a].append(b)

from sys import setrecursionlimit
setrecursionlimit(n + 10)

visited = [False] * (n + 1)
def dfs(adj, visited, order, src):
    if visited[src]:
        return
    visited[src] = True
    for dest in adj[src]:
        dfs(adj, visited, order, dest)
    order.append(src)

order = []
for i in range(1, n + 1):
    dfs(adj, visited, order, i)

print(' '.join(map(str, order[::-1])))