import sys

sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
dp = [0] * n
n_list = [i for i in list(map(int, sys.stdin.readline().split()))]
dp[0] = n_list[0]
for i in range(1, n):
    dp[i] = max(n_list[i], dp[i - 1] + n_list[i])
print(max(dp))
