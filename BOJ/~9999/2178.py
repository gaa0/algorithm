import sys


def bfs(x, y):
    visited[y][x] = 1
    q = [(x, y, 1)]
    while q:
        x, y, dist = q.pop(0)
        if x == M - 1 and y == N - 1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and G[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append((nx, ny, dist + 1))
                visited[ny][nx] = 1


N, M = map(int, sys.stdin.readline().split())
G = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    data = input()
    for j in range(M):
        G[i][j] = int(data[j])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(bfs(0, 0))
