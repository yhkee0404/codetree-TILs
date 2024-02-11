import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(n + 10)

depths = [None] * (n + 1)
depths[0] = 0
depths[1] = 0

def solve(v):
    visited = False
    dw = depths[v] + 1
    for w in adj[v]:
        if depths[w] is None:
            depths[w] = dw
            solve(w)
            visited = True
    if visited:
        depths[v] = 0

solve(1)
ans = 0
for i in range(n + 1):
    if depths[i]:
        ans += depths[i]
print(ans & 1)