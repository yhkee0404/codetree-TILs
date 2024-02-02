with open(0) as f:
    n, *parents, t = map(int, f.read().split())

children = [[] for _ in range(n)]
for i, p in enumerate(parents):
    if p == -1:
        src = i
        if src == t:
            print('0')
            exit()
    elif i != t and p != t:
        children[p].append(i)

ans = 0
stack = [src]
while stack:
    u = stack.pop()
    if not children[u]:
        ans += 1
        continue
    for v in children[u]:
        stack.append(v)
print(ans)