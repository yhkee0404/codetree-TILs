with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        t, a, p = map(int, f.readline().split())
        adj[p].append((i, a if t else - a))

def dfs(adj, src):
    return sum(max(0, a + dfs(adj, u)) for u, a in adj[src])

print(dfs(adj, 1))