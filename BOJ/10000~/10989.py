import sys

N = int(sys.stdin.readline())
x = [0] * 10001
for _ in range(N):
    x[int(sys.stdin.readline())] += 1
for i in range(10001):
    if x[i]:
        for _ in range(x[i]):
            print(i)
