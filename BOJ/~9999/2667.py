import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 and G[ny][nx] == 1:
            visited[ny][nx] = 1
            cnt += 1
            dfs(nx, ny)


N = int(sys.stdin.readline())
G = [[int(inp) for inp in input()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0
cnt_list = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1 and visited[i][j] == 0:
            ans += 1
            cnt = 1
            visited[i][j] = 1
            dfs(j, i)
            cnt_list.append((cnt))
print(ans)
for i in sorted(cnt_list):
    print(i)
