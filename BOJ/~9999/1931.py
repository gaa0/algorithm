import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
f1 = meetings[0][1]
ans = 1
for i in range(1, N):
    if f1 <= meetings[i][0]:
        ans += 1
        f1 = meetings[i][1]
print(ans)
