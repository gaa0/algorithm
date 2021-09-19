import sys

sys.setrecursionlimit(10**9)


def dfs(v):
    global chk
    cnt = 0
    for i in G[v - 1]:
        if visited[i - 1] == 0:
            cnt = 1
            visited[i - 1] = 1
            dfs(i)
    if cnt == 0:
        chk += 1


N, W = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    G[U - 1].append(V)
    G[V - 1].append(U)

chk = 0
visited = [0] * N
visited[0] = 1
dfs(1)

print(W / chk)
