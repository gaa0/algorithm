import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [1] * (N + 1)
ans = 1
for i in range(2, N + 1):
    for j in range(1, i):
        if data[j - 1] < data[i - 1]:
            dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
print(ans)
