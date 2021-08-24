import sys
from collections import deque


def bfs():
    while q:
        cat, x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if cat == '*' and 0 <= nx < C and 0 <= ny < R and G[ny][nx] in ['.', 'S'] and visited[ny][nx] in [0, 2]:
                q.append((cat, nx, ny, dist + 1))
                visited[ny][nx] = 1
                G[ny][nx] = '*'
            elif cat == 'S' and 0 <= nx < C and 0 <= ny < R and G[ny][nx] in ['.', 'D'] and visited[ny][nx] in [0, 4]:
                if G[ny][nx] == 'D':
                    return dist + 1
                chk = 1
                for j in range(4):
                    wx = nx + dx[i]
                    wy = ny + dy[i]
                    if 0 <= wx < C and 0 <= wy < R:
                        if G[wy][wx] == '*':
                            chk = 0
                            break
                        elif G[wy][wx] == 'D':
                            return dist + 2
                if chk == 1:
                    q.append((cat, nx, ny, dist + 1))
                    visited[ny][nx] = 2
                    G[ny][nx] = 'S'
                    G[y][x] = '.'
    return 'KAKTUS'


R, C = map(int, sys.stdin.readline().split())
G = [[inp for inp in input()] for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dx = [0, 0, -1, 1]  # 위, 아래, 왼, 오
dy = [-1, 1, 0, 0]
q = deque()
for i in range(R):
    for j in range(C):
        if G[i][j] == '*':
            q.append(('*', j, i, 0))  # 물
            visited[i][j] = 1
        elif G[i][j] == 'S':
            S = ('S', j, i, 0)  # 고슴도치
            visited[i][j] = 2
        elif G[i][j] == 'X':
            visited[i][j] = 3
        elif G[i][j] == 'D':
            visited[i][j] = 4
q.append(S)
print(bfs())
