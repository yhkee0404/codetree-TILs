with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

def solve(adj, u, v, depth = 0):
    depth += 1
    ans = sum(
        solve(adj, v, w, depth)
        for w in adj[v]
        if w != u
    )
    return ans if ans else depth - 1

print(solve(adj, -1, 1) & 1)