import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
ans = 1000 ** 2 + 1
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(3):  # 1번 집의 색 i
    dp = [1000 ** 2 + 1] * 3
    dp[i] = data[0][i]
    if N == 2:
        a = 1
    else:
        a = N - 2
    for j in range(a):
        tmp_dp = [1000 ** 2 + 1] * 3
        RGB = data[j + 1]
        tmp_dp[0] = RGB[0] + min(dp[1], dp[2])
        tmp_dp[1] = RGB[1] + min(dp[0], dp[2])
        tmp_dp[2] = RGB[2] + min(dp[0], dp[1])
        dp = tmp_dp
    if N >= 3:
        tmp_dp = [1000 ** 2 + 1] * 3
        RGB = data[-1]
        for k in range(3):
            if i != k:
                tmp_dp[k] = RGB[k] + min([dp[x] for x in range(3) if x != k])
        dp = tmp_dp
    ans = min(ans, min(dp))
print(ans)
