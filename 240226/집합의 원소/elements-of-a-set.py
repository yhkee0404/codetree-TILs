ans = []

def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[a] = b

with open(0) as f:
    n, m = map(int, f.readline().split())
    parent = list(range(n + 1))
    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        if a == 0:
            union(parent, b, c)
        else:
            ans.append(
                '1' if find(parent, b) == find(parent, c)
                else '0'
            )

print('\n'.join(ans))