import sys

sys.setrecursionlimit(10**8)


def dfs(v):
    for i in G[v]:
        if ans[i] == 0:
            ans[i] = v
            dfs(i)


N = int(sys.stdin.readline())
parents = {1}
G = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)
dfs(1)
for i in ans[2:]:
    print(i)
