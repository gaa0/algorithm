import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]

ans = 0
for i in range(N - 1, -1, -1):
    ans += K // coin[i]
    K %= coin[i]
print(ans)
