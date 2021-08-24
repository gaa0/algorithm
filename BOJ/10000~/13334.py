import sys
import heapq

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    ho = sorted(list(map(int, sys.stdin.readline().split())))
    people.append(ho)
d = int(sys.stdin.readline())
people.sort(reverse=True)
real_people = []
for i in range(n):
    if people[i][1] - people[i][0] <= d:
        real_people.append(people[i])
ans = 0
heap = []
for i in range(len(real_people)):
    l, r = real_people[i][0], real_people[i][1]
    heapq.heappush(heap, (-r, r))
    std = l + d
    while heap:
        if heap[0][1] > std:
            heapq.heappop(heap)
        else:
            break
    if len(heap) > ans:
        ans = len(heap)
print(ans)
