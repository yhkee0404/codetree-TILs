with open(0) as f:
    m, *nodes = map(int, f.read().split())

def solve(m, nodes):
    
    ss = nodes[::2]
    es = nodes[1::2] 
    max_s = max(s for s in ss)
    max_e = max(e for e in es)
    
    visited = [False] * (max(max_s, max_e) + 1)
    
    for e in es:
        visited[e] = True
    root = None
    for s in ss:
        if visited[s]:
            continue
        if root is not None:
            return False
        root = s
        visited[s] = True
    
    adj = [[] for _ in visited]
    for i in range(0, m << 1, 2):
        adj[nodes[i]].append(nodes[i | 1])
    
    stack = [root]
    for i in range(len(visited)):
        visited[i] = False
    visited[root] = True
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if visited[v]:
                return False
            visited[v] = True
            stack.append(v)
    return all(v for v in visited[1:])

print(1 if solve(m, nodes) else 0)