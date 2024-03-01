with open(0) as f:
    n, *arr = map(int, f.read().split())

ldp = [0] * (n + 1)
for i in range(n):
    ldp[i + 1] = ldp[i] + arr[i]

def merge(l, r, arr, ldp, dp):
    if dp[l][r] is not None:
        return dp[l][r]
    if l + 1 == r:
        return 0
    ans = 5_000_000_000
    for i in range(l + 1, r):
        ans = min(ans, merge(l, i, arr, ldp, dp) + merge(i, r, arr, ldp, dp))
    ans += ldp[r] - ldp[l]
    dp[l][r] = ans
    return ans

dp = [[None] * (n + 1) for _ in range(n)]
print(merge(0, n, arr, ldp, dp))