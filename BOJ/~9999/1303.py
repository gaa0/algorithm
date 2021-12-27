import sys

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

war = []
for _ in range(M):
    war.append([s for s in input()])

visited = [[0] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == 0 and war[ny][nx] == war[y][x]:
            visited[ny][nx] = 1
            cnt += 1
            dfs(nx, ny)


W = 0
B = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(j, i)
            if war[i][j] == 'W':
                W += cnt ** 2
            else:
                B += cnt ** 2

print(W, B)
