from heapq import heappush, heappop

with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        adj[a].append((b, c))
        adj[b].append((a, c))

dist = [1_000_000_000] * (n + 1)
dist[1] = 1
pq = [(1, 1)]
while pq:
    du, u = heappop(pq)
    if du != dist[u]:
        continue
    dist[u] = - dist[u]
    for v, w in adj[u]:
        if w < dist[v]:
            dist[v] = w
            heappush(pq, (w, v))

print(- sum(dist) + 1_000_000_000 - 1)