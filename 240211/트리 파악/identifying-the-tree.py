import sys
sys.setrecursionlimit(200000)

n = int(input().strip())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

depths = [None] * (n + 1)
depths[0] = 0
depths[1] = 0

ans = 0
def solve(v):
    global ans
    visited = False
    dw = depths[v] + 1
    for w in adj[v]:
        if depths[w] is None:
            depths[w] = dw
            solve(w)
            visited = True
    if not visited:
        ans += depths[v]

solve(1)
print(ans & 1)