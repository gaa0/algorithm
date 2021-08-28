import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dp = [10 ** 6] * (N + 1)
dp[1] = 0
for i in range(1, N + 1):
    op = [i * 3, i * 2, i + 1]
    for o in op:
        if o <= N and dp[i] + 1 < dp[o]:
            dp[o] = dp[i] + 1
print(dp[N])
