import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dp = [[0] * 21 for _ in range(N - 1)]
data = list(map(int, sys.stdin.readline().split()))
dp[0][data[0]] = 1
for i in range(N - 2):
    for j in range(21):
        if dp[i][j] >= 1:
            a = j + data[i + 1]
            b = j - data[i + 1]
            if 0 <= a <= 20: dp[i + 1][a] += dp[i][j]
            if 0 <= b <= 20: dp[i + 1][b] += dp[i][j]
print(dp[-1][data[-1]])
