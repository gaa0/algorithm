import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for j in range(1, N):
    for i in range(j - 1, -1, -1):
        tmp_dp = float('inf')
        for k in range(i, j):
            x = dp[i][k] + dp[k + 1][j] + M[i][0] * M[k][1] * M[j][1]
            if x < tmp_dp:
                tmp_dp = x
        dp[i][j] = tmp_dp
print(dp[0][N - 1])
