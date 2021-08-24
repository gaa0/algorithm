import sys
import heapq

N = int(sys.stdin.readline())
x = int(sys.stdin.readline())
min_heap = []
max_heap = [(-x, x)]
print(max_heap[0][1])
i = N - 1
while i:
    x = int(sys.stdin.readline())

    if x > max_heap[0][1]:
        heapq.heappush(min_heap, x)
    else:
        heapq.heappush(max_heap, (-x, x))

    if len(min_heap) > len(max_heap):
        x = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-x, x))
    elif len(min_heap) < len(max_heap) - 1:
        x = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, x)
    print(max_heap[0][1])
    i -= 1
