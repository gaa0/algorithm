import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dp = [None for _ in range(N + 1)]
dp[1] = (1, 0)  # 1로 끝나는 수의 개수, 0으로 끝나는 수의 개수
if N >= 2: dp[2] = (0, 1)
if N >= 3: dp[3] = (1, 1)
if N >= 4:
    for i in range(4, N + 1):
        dp[i] = (dp[i - 1][1], dp[i - 1][0] + dp[i - 1][1])
print(sum(dp[N]))
