import sys


def dummy(N):
    t, d, r, c = 0, 0, 1, 1
    len_baam = 1
    while 1 <= r <= N and 1 <= c <= N:
        if (t, 'L') in baam or (t, 'D') in baam:
            tmp = baam.pop(0)
            if tmp[1] == 'L':
                d -= 1
            else:
                d += 1
            d = d % 4
        t += 1
        next_x = r + x_list[d]
        next_y = c + y_list[d]
        if 1 <= next_x <= N and 1 <= next_y <= N and (next_x, next_y) not in que:
            r = next_x
            c = next_y
            que.append((r, c))
            if (c, r) in apple:
                apple.remove((c, r))
                len_baam += 1
            else:
                que.pop(0)
        else:
            return t
    return t


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple = []
for _ in range(K):
    apple.append(tuple(map(int, sys.stdin.readline().split())))
L = int(sys.stdin.readline())
baam = []
for _ in range(L):
    x, y = map(str, sys.stdin.readline().split())
    baam.append((int(x), y))
que = [(1, 1)]
x_list = [1, 0, -1, 0]  # 우하좌상
y_list = [0, 1, 0, -1]
print(dummy(N))
