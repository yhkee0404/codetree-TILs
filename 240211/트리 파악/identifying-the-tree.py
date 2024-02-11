import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(max(10, n))
depths = {1: 0}

def solve(v):
    visited = False
    dw = depths[v] + 1
    for w in adj[v]:
        if w not in depths:
            depths[w] = dw
            solve(w)
            visited = True
    if visited:
        depths[v] = 0

solve(1)
print(sum(depths.values()) & 1)