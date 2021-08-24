import sys


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, N + 1):
        if G[v][i] == 1 and visited[i] == 0:
            dfs(i)


def bfs(v):
    print(v, end=' ')
    visited[v] = 1
    q = [v]
    while q:
        v = q.pop(0)
        for i in range(1, N + 1):
            if G[v][i] == 1 and visited[i] == 0:
                print(i, end=' ')
                visited[i] = 1
                q.append(i)


N, M, V = map(int, sys.stdin.readline().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    G[x][y] = G[y][x] = 1
visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
