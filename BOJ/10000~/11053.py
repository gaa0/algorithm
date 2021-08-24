import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
DP = [1] * N
for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            x = DP[j] + 1
            if x > DP[i]:
                DP[i] = x
print(max(DP))
