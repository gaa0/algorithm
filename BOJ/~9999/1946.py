import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    data = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])
    ans = 1
    second = data[0][1]
    for i in range(1, N):
        if data[i][1] < second:
            ans += 1
            second = data[i][1]
    print(ans)
