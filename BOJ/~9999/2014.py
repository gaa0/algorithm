import sys
import heapq

sys.stdin = open('input.txt')

K, N = map(int, sys.stdin.readline().split())
prime = list(map(int, sys.stdin.readline().split()))

# 우선순위 큐  * prime 리스트랑 따로 만들기 *
pq = []
for p in prime:
    heapq.heappush(pq, p)

ans = 0
for _ in range(N):
    ans = heapq.heappop(pq)
    for p in prime:
        heapq.heappush(pq, ans * p)
        if ans % p == 0:
            break
print(ans)
