with open(0) as f:
    n, *parents, t = map(int, f.read().split())

children = [[] for _ in range(n)]
for i, p in enumerate(parents):
    if p == -1:
        src = i
    else:
        children[p].append(i)

ans = 0
stack = [src]
while stack:
    u = stack.pop()
    cnt = 0
    for v in children[u]:
        if v == t:
            continue
        stack.append(v)
        cnt += 1
    if not cnt:
        ans += 1
print(ans)