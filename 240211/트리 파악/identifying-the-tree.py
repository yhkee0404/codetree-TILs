with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

def solve(adj):
    ans = 0
    stack = [(-1, 1, 0)]
    while stack:
        u, v, depth = stack.pop()
        depth += 1
        pushed = False
        for w in adj[v]:
            if w != u:
                stack.append((v, w, depth))
                pushed = True
        if not pushed:
            ans += depth - 1
    return ans

print(solve(adj) & 1)