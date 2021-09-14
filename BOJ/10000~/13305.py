import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

ans = 0
price = cost[0]

for i in range(N - 1):
    ans += price * road[i]
    if price > cost[i + 1]:
        price = cost[i + 1]

print(ans)
