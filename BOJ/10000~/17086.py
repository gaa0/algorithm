import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, -1, 1, 1]
q = deque()
ans = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            q.append((j, i, 1))
while q:
    x, y, dist = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and G[ny][nx] == 0:
            G[ny][nx] = dist
            ans = max(ans, dist)
            q.append((nx, ny, dist + 1))
print(ans)
