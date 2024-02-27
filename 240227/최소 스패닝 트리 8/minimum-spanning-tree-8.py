with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[500_000] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        c = min(c, adj[a][b])
        adj[a][b] = c
        adj[b][a] = c

def findSource(n, dist):
    dj = 500_000
    j = 0
    for i in range(1, n + 1):
        di = dist[i]
        if 1 <= di < dj:
            dj = di
            j = i
    return j

dist = [500_000] * (n + 1)
dist[1] = 1
while True:
    src = findSource(n, dist)
    if not src:
        break
    dist[src] = - dist[src]
    ai = adj[src]
    for i in range(1, n + 1):
        dist[i] = min(dist[i], ai[i])

print(- sum(dist) + 500_000 - 1)