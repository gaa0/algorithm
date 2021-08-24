import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
indegree = [0] * (N + 1)
G = [[] for _ in range(N + 1)]
dp = [defaultdict(int) for _ in range(N + 1)]
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    G[Y].append((X, K))
    indegree[X] += 1


def topology_sort():
    q = deque()
    basic = set()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            basic.add(i)
    while q:
        now = q.popleft()
        for j in range(len(G[now])):
            x, y = G[now][j]
            indegree[x] -= 1
            if now in basic:
                dp[x][now] += y
            else:
                for k, v in dp[now].items():
                    dp[x][k] += v * y
            if indegree[x] == 0:
                q.append(x)
    for k, v in sorted(dp[-1].items()):
        print(k, v)


topology_sort()
