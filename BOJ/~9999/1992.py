import sys

sys.stdin = open('2_input.txt')

N = int(sys.stdin.readline())
G = [[i for i in input()] for _ in range(N)]


def re(x, y, q):
    global ans
    point = G[y][x]
    chk = 0
    for j in range(y, y + q):
        for i in range(x, x + q):
            if point != G[j][i]:
                chk = 1
                break
        if chk == 1:
            break
    if chk == 1:
        ans += '('
        q //= 2
        re(x, y, q)
        re(x + q, y, q)
        re(x, y + q, q)
        re(x + q, y + q, q)
        ans += ')'
    else:
        ans += point


ans = ''
re(0, 0, N)
print(ans)
