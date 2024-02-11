import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(n + 10)

def solve(adj, u, v, depth = 0):
    depth += 1
    ans = 0
    for w in adj[v]:
        if w != u:
            ans += solve(adj, v, w, depth)
    return ans if ans else depth - 1

print(solve(adj, -1, 1) & 1)