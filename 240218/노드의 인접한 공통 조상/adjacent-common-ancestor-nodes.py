with open(0) as f:
    n = int(f.readline().strip())
    parent = [None] * (n + 1)
    children = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        parent[b] = a
        children[a].append(b)
    a, b = map(int, f.read().split())

def find_root(n, parent):
    for i in range(1, n + 1):
        if parent[i] is None:
            return i

src = find_root(n, parent)

def find_level(n, children, src, level):
    l = level[src] + 1
    for u in children[src]:
        level[u] = l
        find_level(n, children, u, level)

level = [0] * (n + 1)
find_level(n, children, src, level)

while True:
    diff = level[a] - level[b]
    if diff == 0:
        break
    if diff < 0:
        b = parent[b]
    else:
        a = parent[a]

while a != b:
    a = parent[a]
    b = parent[b]

print(a)