with open(0) as f:
    n = int(f.readline().strip())
    adj = {}
    for _ in range(n):
        a, b, c = f.readline().split()
        adj[a] = [b, c]

def preorder_traverse(adj, src, ans):
    if src == '.':
        return
    ans.append(src)
    for u in adj[src]:
        preorder_traverse(adj, u, ans)
    return ans

def inorder_traverse(adj, src, ans):
    if src == '.':
        return
    inorder_traverse(adj, adj[src][0], ans)
    ans.append(src)
    inorder_traverse(adj, adj[src][1], ans)
    return ans

def postorder_traverse(adj, src, ans):
    if src == '.':
        return
    for u in adj[src]:
        postorder_traverse(adj, u, ans)
    ans.append(src)
    return ans

print(
    '\n'.join(
        ''.join(traverse(adj, 'A', []))
        for traverse in (preorder_traverse, inorder_traverse, postorder_traverse)
    )
)