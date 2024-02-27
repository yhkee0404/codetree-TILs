with open(0) as f:
    n = int(f.readline().strip())
    adj_t = [[]]
    in_degrees = [None] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        d, m, *a = map(int, f.readline().split())
        adj_t.append(a)
        in_degrees[i] = m
        dp[i] = d

adj = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for a in adj_t[i]:
        adj[a].append(i)

q = []
for i in range(1, n + 1):
    if not in_degrees[i]:
        q.append(i)

head = 0
while head != len(q):
    u = q[head]
    head += 1
    dp[u] += max(0, 0, *(dp[v] for v in adj_t[u]),)
    for v in adj[u]:
        in_degrees[v] -= 1
        if not in_degrees[v]:
            q.append(v)

print(max(dp))