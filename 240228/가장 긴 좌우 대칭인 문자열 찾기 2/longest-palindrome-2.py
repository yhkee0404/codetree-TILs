with open(0) as f:
    s = f.read().strip()

arr = [None]
for c in s:
    arr.append(c)
    arr.append(None)

dp = [None] * len(arr)
r, p = -1, -1
for i in range(len(arr)):
    diff = r - i
    a = 0 if diff <= 0 \
        else min(diff, dp[(p << 1) - i])
    j, k = i - a, i + a
    while True:
        nj = j - 1
        nk = k + 1
        if nj == -1 or nk == len(arr) \
                or arr[nj] != arr[nk]:
            break
        j = nj
        k = nk
        a += 1
    dp[i] = a
    if r < k:
        r = k
        p = i

print(max(dp))