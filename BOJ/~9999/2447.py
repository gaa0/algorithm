import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

ans = [[0] * N for _ in range(N)]


def star(N, x, y):
    if N > 3:
        next_N = N // 3
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    star(next_N, x + next_N * i, y + next_N * j)
    else:
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    ans[x + i][y + j] = 1


star(N, 0, 0)
for i in range(N):
    for j in range(N):
        if ans[i][j] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
