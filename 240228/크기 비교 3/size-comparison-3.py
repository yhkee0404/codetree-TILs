from heapq import heappush, heappop, heapify

with open(0) as f:
    n, m = map(int, f.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, f.readline().split())
        adj[a].append(b)

in_degrees = [0] * (n + 1)
for a in adj:
    for b in a:
        in_degrees[b] += 1

ans = []
pq = []
for i in range(1, n + 1):
    if not in_degrees[i]:
        pq.append(i)
heapify(pq)
while pq:
    u = heappop(pq)
    ans.append(u)
    for v in adj[u]:
        in_degrees[v] -= 1
        if in_degrees[v] == 0:
            heappush(pq, v)

print(' '.join(map(str, ans)))