import sys
import heapq

sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

heapq.heapify(data)
for _ in range(m):
    x = heapq.heappop(data)
    y = heapq.heappop(data)
    sum_xy = x + y
    heapq.heappush(data, sum_xy)
    heapq.heappush(data, sum_xy)
print(sum(data))
