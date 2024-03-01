with open(0) as f:
    t, p = map(lambda s: list(map(lambda c: ord(c) + 1, s)), f.read().split())

def rabin_karp(
    t, p,
    p_ = (29, 31),
    m = (1_000_000_007, 1_000_000_009),
):
    if len(t) < len(p):
        return -1
    pp = []
    p_h = []
    t_h = []
    for k in range(2):
        mk = m[k]
        pk = p_[k]
        ph = 0
        th = 0
        ppi = 1
        for i in range(len(p) - 1, -1, -1):
            ph = (ph + p[i] * ppi) % mk
            th = (th + t[i] * ppi) % mk
            ppi = ppi * pk % mk
        pp.append(ppi)
        p_h.append(ph)
        t_h.append(th)
    if p_h == t_h:
        return 0
    l = 0
    r = len(p)
    while r != len(t):
        for k in range(2):
            t_h[k] = (t_h[k] * p_[k] - t[l] * pp[k] + t[r]) % m[k]
        if p_h == t_h:
            return l + 1
        l += 1
        r += 1
    return -1

print(rabin_karp(t, p))