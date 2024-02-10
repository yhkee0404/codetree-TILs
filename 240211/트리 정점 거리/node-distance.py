import sys

write = sys.stdout.write

def visit(adj, a, dist):
    da = dist[a]
    for b, w in adj[a]:
        if b not in dist:
            dist[b] = da + w
            visit(adj, b, dist)
    return dist

with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, f.readline().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    dist = [visit(adj, i, {i: 0}) for i in range(0, n + 1)]
    for _ in range(m):
        a, b = map(int, f.readline().split())
        write(f'{dist[a][b]}\n')