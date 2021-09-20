from collections import deque


def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    dx, dy = [1, 0], [0, 1]
    for puddle in puddles:
        x, y = puddle
        visited[y][x] = 1

    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx < m + 1 and 1 <= ny < n + 1 and visited[ny][nx] == 0 and [nx, ny] not in puddles:
                if [nx, ny] not in puddles:
                    dp[ny][nx] = (dp[ny - 1][nx] + dp[ny][nx - 1]) % 1000000007
                visited[ny][nx] = 1
                q.append((nx, ny))

    return dp[n][m] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
