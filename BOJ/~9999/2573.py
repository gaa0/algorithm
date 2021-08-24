import sys


def melt():
    melt_dict = dict()
    visited = [[0] * M for _ in range(N)]
    visited[iceberg[0][1]][iceberg[0][0]] = 1
    stk = [iceberg[0]]
    selected_cnt = 0
    while stk:
        x, y = stk.pop()
        selected_cnt += 1
        melting_cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[ny][nx] == 0:
                if data[ny][nx] == 0:
                    melting_cnt += 1
                elif data[ny][nx] != 0:
                    visited[ny][nx] = 1
                    stk.append((nx, ny))
        melt_dict[(x, y)] = melting_cnt
    new_iceberg = []
    for k, v in melt_dict.items():
        x, y = k
        data[y][x] = max(0, data[y][x] - v)
        if data[y][x] > 0:
            new_iceberg.append((x, y))

    return selected_cnt, new_iceberg

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # 동서남북

iceberg = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if data[i][j] != 0:
            iceberg.append((j, i))
cnt = -1
while 1:
    cnt += 1
    selected_cnt, new_iceberg = melt()
    if len(iceberg) != selected_cnt:
        print(cnt)
        break
    if not new_iceberg:
        print(0)
        break
    iceberg = new_iceberg[:]
