import sys
from collections import deque


def bfs():
    result = 0
    while q:
        x, y, z, dist = q.popleft()
        if dist > result:
            result = dist
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and data[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                q.append((nx, ny, nz, dist + 1))
                visited[nz][ny][nx] = 1
    return result


M, N, H = map(int, sys.stdin.readline().split())
data = []
visited = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    data.append(tmp)
    visited.append(tmp)
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]  # 위, 아래, 왼, 오, 앞, 뒤
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1:
                q.append((k, j, i, 0))
answer = bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == 0:
                answer = -1
                break
        if answer == -1:
            break
    if answer == -1:
        break
print(answer)
