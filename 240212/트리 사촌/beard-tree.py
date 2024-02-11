with open(0) as f:
    n, k, *arr = map(int, f.read().split())

children = []
i = 1
src = None
while i != n:
    ci = [i]
    found = False
    if arr[i] == k:
        found = True
    j = i + 1
    while j != n and arr[j] - arr[j - 1] == 1:
        ci.append(j)
        if not found and arr[j] == k:
            found = True
        j += 1
    children.append(ci)
    if found:
        src = len(children) - 1
    i = j

for ci in children:
    if ci[0] <= src <= ci[-1]:
        break
ans = sum(
    len(children[u])
    for u in ci
    if u != src
)
print(ans)