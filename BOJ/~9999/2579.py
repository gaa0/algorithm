import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [i for i in arr]

if N >= 2:
    dp[1] += dp[0]

if N >= 3:
    dp[2] = max(dp[0] + dp[2], arr[1] + dp[2])

if N >= 4:
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])

print(dp[-1])
