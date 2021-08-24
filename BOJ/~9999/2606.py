import sys


def dfs(v):
    visited[v] = 1
    for i in range(1, N + 1):
        if G[v][i] == 1 and visited[i] == 0:
            dfs(i)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    G[x][y] = G[y][x] = 1
visited = [0] * (N + 1)
dfs(1)
print(sum(visited) - 1)
