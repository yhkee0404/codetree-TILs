import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(n + 10)
visited = set()

def solve(v, depth = 0):
    visited.add(v)
    depth += 1
    ans = 0
    for w in adj[v]:
        if w not in visited:
            ans += solve(w, depth)
    visited.remove(v)
    return ans if ans else depth - 1

print(solve(1) & 1)