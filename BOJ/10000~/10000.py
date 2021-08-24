import sys

N = int(sys.stdin.readline())
stk = []
one = []
for _ in range(N):
    c, r = map(int, sys.stdin.readline().split())
    one.append((c - r, 0))  # 왼쪽 좌표 0
    one.append((c + r, 1))  # 오른쪽 좌표 1
one = sorted(one, key=lambda x: (x[0], -x[1]))
cnt = 1
for o in one:
    if o[1] == 0:
        stk.append(o)
    elif o[1] == 1:
        c = 0
        while 1:
            x = stk.pop()
            if x[1] == 0:
                if c:
                    if o[0] - x[0] == c:
                        cnt += 2
                    else:
                        cnt += 1
                else:
                    cnt += 1
                stk.append((o[0] - x[0], 2))  # 길이 2
                break
            elif x[1] == 2:
                c += x[0]
print(cnt)
