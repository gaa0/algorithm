import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
data = [G, [[0] * N for _ in range(N)]]
for i in range(N):
    for j in range(N):
        data[1][j][i] = G[i][j]


def available(s, e):
    cnt = [0, 0, 0]
    for i in range(s[0], e[0] + 1):
        for j in range(s[1], e[1] + 1):
            cnt[G[i][j]] += 1
    if cnt[2] == 0:
        return 0
    if cnt[2] == 1:
        if cnt[1] == 0:
            return 1
        else:
            return 0
    if cnt[1] == 0:
        return 0
    return 2


def cut(s, e, d):
    k = available(s, e)
    if k == 0:
        return 0
    elif k == 1:
        return 1

    result = 0
    for u in range(s[1 - d] + 1, e[1 - d]):
        possible = False
        for v in range(s[d], e[d] + 1):
            if data[1 - d][u][v] == 2:
                possible = False
                break
            if data[1 - d][u][v] == 1:
                possible = True
        if not possible:
            continue

        tmp1 = [[e[0], u - 1], [u - 1, e[1]]]
        tmp2 = [[s[0], u + 1], [u + 1, s[1]]]

        first = cut(s, tmp1[d], 1 - d)
        if first == 0:
            continue

        second = cut(tmp2[d], e, 1 - d)
        if second == 0:
            continue

        result += first * second
    return result


start = [0, 0]
end = [N - 1, N - 1]

ans = cut(start, end, 1) + cut(start, end, 0)

if ans == 0:
    ans = -1

print(ans)
