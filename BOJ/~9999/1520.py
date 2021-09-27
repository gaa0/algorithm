import sys

sys.stdin = open('input_2.txt')


def dfs(x, y):
    global ans
    if x == N - 1 and y == M - 1:
        return 1
    elif dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and G[y][x] > G[ny][nx]:
                dp[y][x] += dfs(nx, ny)

    return dp[y][x]


M, N = map(int, sys.stdin.readline().split())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # 상하좌우

ans = 0
print(dfs(0, 0))
