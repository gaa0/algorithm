import sys


def dfs(x, y, cnt):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and done[G[ny][nx]] == 0:
            if cnt + 1 > ans:
                ans = cnt + 1
                if ans == 26:
                    print(26)
                    exit(0)
            done[G[ny][nx]] = 1
            dfs(nx, ny, cnt + 1)
            done[G[ny][nx]] = 0


R, C = map(int, sys.stdin.readline().split())
G = [list(map(lambda x: ord(x) - 65, input())) for _ in range(R)]
done = [0] * 26
done[G[0][0]] = 1
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
ans = 1
dfs(0, 0, 1)
print(ans)
