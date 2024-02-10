import sys
from heapq import heappush, heappop

write = sys.stdout.write

def visit(adj, a, dist):
    pq = [(0, a)]
    while pq:
        du, u = heappop(pq)
        if du != dist[u]:
            continue
        for v, w in adj[u]:
            dv = du + w
            if dv < dist.get(v, 1_000_001):
                dist[v] = dv
                heappush(pq, (dv, v))
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