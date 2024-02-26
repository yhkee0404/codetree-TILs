with open(0) as f:
    n, m = map(int, f.readline().split())
    edges = []
    for _ in range(m):
        abc = tuple(map(int, f.readline().split()))
        edges.append(abc)

edges.sort(key = lambda abc: abc[-1])

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    diff = rank[a] - rank[b]
    if diff < 0:
        a, b = b, a
    if diff == 0:
        rank[a] += 1
    parent[b] = a

def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]

ans = 0
parent = list(range(n + 1))
rank = [0] * (n + 1)
for a, b, c in edges:
    if find(parent, a) == find(parent, b):
        continue
    union(parent, rank, a, b)
    ans += c

print(ans)