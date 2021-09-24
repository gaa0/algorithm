import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**4)

n = int(sys.stdin.readline())
# G = [[0] * (n + 1) for _ in range(n + 1)]
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().split())
    # G[p][c] = w
    # G[c][p] = w
    G[p].append([c, w])
    G[c].append([p, w])


def dfs(v, dist):
    global first, first_dist
    if dist > first_dist:
        first_dist = dist
        first = v
    for i in G[v]:
        if i[0] != 0 and visited[i[0]] == 0:
            visited[i[0]] = 1
            dfs(i[0], dist + i[1])


visited = [0] * (n + 1)
visited[1] = 1
first = 0
first_dist = 0
dfs(1, 0)
visited = [0] * (n + 1)
visited[first] = 1
first_dist = 0
dfs(first, 0)
print(first_dist)
