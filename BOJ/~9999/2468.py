import sys

sys.setrecursionlimit(10**8)

def dfs(j, k):
    for i in range(4):
        next_x = j + x_list[i]
        next_y = k + y_list[i]
        if 0 <= next_x < N and 0 <= next_y < N and G[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
            x = next_x
            y = next_y
            visited[y][x] = 1
            dfs(x, y)

N = int(sys.stdin.readline())
data = []
high = {0}

x_list = [1, 0, -1, 0]  # 우하좌상
y_list = [0, 1, 0, -1]

for _ in range(N):
    tmp_data = list(map(int, sys.stdin.readline().split()))
    data.append(tmp_data)
    high.update(tmp_data)
ans = 0
for i in list(high):
    tmp_ans = 0
    G = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if data[y][x] > i:
                G[y][x] = 1
    for j in range(N):
        for k in range(N):
            if G[j][k] == 1 and visited[j][k] == 0:
                tmp_ans += 1
                visited[j][k] = 1
                dfs(k, j)
    if tmp_ans > ans:
        ans = tmp_ans

print(ans)