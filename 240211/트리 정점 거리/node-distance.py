import sys

write = sys.stdout.write

def visit(adj, a, dist):
    da = dist[a]
    for b, w in adj[a]:
        db = da + w
        if db < dist.get(b, 999_001):
            dist[b] = db
            visit(adj, b, dist)
    return dist

with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, f.readline().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    for _ in range(m):
        a, b = map(int, f.readline().split())
        write(f'{visit(adj, a, {a: 0})[b]}\n')