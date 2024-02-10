import sys

write = sys.stdout.write

def visit(adj, a, dist):
    da = dist[a]
    for b, w in adj[a]:
        if dist[b] is None:
            dist[b] = da + w
            visit(adj, b, dist)

with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, f.readline().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    dist = [[None] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        di = dist[i]
        di[i] = 0
        visit(adj, i, di)
    for _ in range(m):
        a, b = map(int, f.readline().split())
        write(f'{dist[a][b]}\n')