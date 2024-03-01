ans = []

bit = 0
with open(0) as f:
    q = int(f.readline().strip())
    for _ in range(q):
        cmd, *args = f.readline().strip().split()
        match cmd[0]:
            case 'a':
                bit |= 1 << int(args[0])
            case 'd':
                bit &= ~ 1 << int(args[0])
            case 'p':
                ans.append('1' if bit & (1 << int(args[0])) else '0')
            case 't':
                bit ^= 1 << int(args[0])
            case 'c':
                bit = 0

print('\n'.join(ans))