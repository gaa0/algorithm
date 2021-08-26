import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 1000001
q = deque([(N, 0)])
while q:
    n, t = q.popleft()
    if n == K:
        print(t)
        exit(0)
    if 0 <= n - 1 <= 100000 and visited[n - 1] == 0:
        visited[n - 1] = 1
        q.append((n - 1, t + 1))
    if 0 <= n + 1 <= 100000 and visited[n + 1] == 0:
        visited[n + 1] = 1
        q.append((n + 1, t + 1))
    if 0 <= 2 * n <= 100000 and visited[2 * n] == 0:
        visited[2 * n] = 1
        q.append((2 * n, t + 1))
