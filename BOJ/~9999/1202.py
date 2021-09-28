import sys
import heapq

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
j = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], reverse=True)
bags = sorted([int(sys.stdin.readline()) for _ in range(K)])

q = []
ans = 0

for bag in bags:
    while j:
        if j[-1][0] <= bag:
            x = j.pop()
            heapq.heappush(q, (-x[1], x[1]))
        else:
            break
    if q:
        ans += heapq.heappop(q)[1]

print(ans)
