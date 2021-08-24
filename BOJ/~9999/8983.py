import sys

M, N, L = map(int, sys.stdin.readline().split())
point_list = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pl = 0
    pr = M - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        d = abs(point_list[pc] - a) + b
        if d <= L:
            ans += 1
            break
        else:
            if point_list[pc] == a:
                break
            elif point_list[pc] > a:
                pr = pc - 1
            else:
                pl = pc + 1
print(ans)
