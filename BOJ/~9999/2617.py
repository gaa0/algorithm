import sys


def dfs(v):
    global ans, flag
    if flag:
        return
    for i in range(1, N + 1):
        if G[v][i] == 1 and visited[i] == 0:
            light_set.add(i)
            if len(light_set) >= (N + 1) // 2:
                flag = True
                return
            visited[i] = 1
            dfs(i)


def dfs2(v):
    global ans, flag2
    if flag2:
        return
    for i in range(1, N + 1):
        if G[i][v] == 1 and visited2[i] == 0:
            weight_set.add(i)
            if len(weight_set) >= (N + 1) // 2:
                flag2 = True
                return
            visited2[i] = 1
            dfs2(i)


N, M = map(int, sys.stdin.readline().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
ans = 0
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    G[x][y] = 1
for i in range(1, N + 1):  # i보다 가벼운/무거운 구슬 3개 이상인지 찾기
    light_set = set()
    weight_set = set()
    flag = flag2 = False
    visited = [0] * (N + 1)
    visited2 = [0] * (N + 1)
    visited[i] = visited2[i] = 1
    dfs(i)
    dfs2(i)
    if len(light_set) >= (N + 1) // 2 or len(weight_set) >= (N + 1) // 2:
        ans += 1

print(ans)
