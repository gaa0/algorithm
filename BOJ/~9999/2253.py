import sys

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
max_v = int((2 * N + 0.25) ** 0.5 - 0.5) + 2
INF = float('inf')
dp = [[INF] * max_v for _ in range(N + 1)]
small = {int(sys.stdin.readline()) for _ in range(M)}
dp[2][1] = 1
for i in range(2, N):
    for j in range(max_v):
        if dp[i][j] != INF:
            op = [j - 1, j, j + 1]
            for o in op:
                if i + o not in small and 1 <= o < max_v and i + o <= N and dp[i][j] + 1 < dp[i + o][o]:
                    dp[i + o][o] = dp[i][j] + 1

ans = min(dp[N])
if ans == INF: ans = -1
print(ans)
