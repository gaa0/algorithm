import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    tmp_dp = [i for i in dp]
    for i in range(K - W + 1):
        if i + W <= K:
            tmp_dp[i + W] = max(dp[i + W], dp[i] + V)
    dp = tmp_dp
print(max(dp))
