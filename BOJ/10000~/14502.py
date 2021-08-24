def bfs(x, y):
    q = [[x, y]]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and dc[x+dx[i]][y+dy[i]] == 0:
                a = x+dx[i]
                b = y+dy[i]
                dc[a][b] = 2
                q.append([a, b])



import itertools
import copy
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]  ## 상우하좌
dy = [0, 1, 0, -1]
zero = []
two = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            zero.append((i, j))
        elif data[i][j] == 2:
            two.append((i, j))
zl = list(itertools.combinations(zero, 3))
c = []
for i in zl:
    dc = copy.deepcopy(data)
    for j in i:
        dc[j[0]][j[1]] = 1
    for k in two:
        bfs(k[0], k[1])
    cnt = 0
    for xx in range(N):
        for yy in range(M):
            if dc[xx][yy] == 0:
                cnt += 1
        c.append(cnt)
print(max(c))