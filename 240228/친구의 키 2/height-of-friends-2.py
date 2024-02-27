with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, f.readline().split())
        adj[a].append(b)

def dfs(adj, color, src):
    c = color[src]
    if c == 1:
        return False
    if c == 2:
        return True
    color[src] = 1
    for dest in adj[src]:
        if not dfs(adj, color, dest):
            return False
    color[src] = 2
    return True

color = [0] * (n + 1)
print('Consistent' if all(dfs(adj, color, i) for i in range(1, n + 1)) else 'Inconsistent')