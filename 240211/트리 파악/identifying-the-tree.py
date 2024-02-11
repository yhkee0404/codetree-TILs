import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(n + 10)
depths = {1: 0}

def solve(v):
    ans = 0
    dv = depths[v]
    for w in adj[v]:
        if w not in depths:
            depths[w] = dv + 1
            ans += solve(w)
    return ans if ans else dv

print(solve(1) & 1)