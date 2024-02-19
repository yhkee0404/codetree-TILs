from sys import setrecursionlimit as srl

def init_parents(n, adj, parents, depths, src):
    du = depths[src] + 1
    for u in adj[src]:
        if depths[u] is None:
            depths[u] = du
            parents[0][u] = src
            init_parents(n, adj, parents, depths, u)

def make_parents(n, adj):
    parents = [[None] * (n + 1) for _ in range(16)]
    depths = [None] * (n + 1)
    depths[1] = 0
    init_parents(n, adj, parents, depths, 1)
    di = 1
    for i in range(1, 16):
        pu, pv = parents[i - 1: i + 1]
        for j in range(2, n + 1):
            if depths[j] >= di:
                pv[j] = pu[pu[j]]
        di <<= 1
    return parents, depths

def lca(parents, depths, a, b):
    da = depths[a]
    db = depths[b]
    diff = da - db
    if diff < 0:
        a, b, da, db = b, a, db, da
        diff = - diff
    i = 0
    while diff:
        if diff & 1:
            a = parents[i][a]
        i += 1
        diff >>= 1
    if a == b:
        return a
    i = 1 << 16
    for j in range(15, -1, -1):
        i >>= 1
        if i > db:
            continue
        pj = parents[j]
        if pj[a] == pj[b]:
            continue
        a = pj[a]
        b = pj[b]
        db = depths[a]
    return parents[0][a]

with open(0) as f:
    n = int(f.readline().strip())
    srl(n + 10)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    parents, depths = make_parents(n, adj)
    q = int(f.readline().strip())
    ans = []
    for _ in range(q):
        a, b = map(int, f.readline().split())
        ans.append(lca(parents, depths, a, b))

print('\n'.join(map(str, ans)))