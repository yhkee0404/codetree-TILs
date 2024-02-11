import sys
sys.setrecursionlimit(100000)

n = int(input().strip())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

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
print(sum(depths) & 1)