import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
ans = 0
while len(heap) >= 2:
    tmp = 0
    tmp += heapq.heappop(heap)
    tmp += heapq.heappop(heap)
    ans += tmp
    heapq.heappush(heap, tmp)
print(ans)