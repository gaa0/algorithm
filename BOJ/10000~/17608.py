import sys

N = int(sys.stdin.readline())
stk = []
for _ in range(N):
    stk.append(int(sys.stdin.readline()))
right = stk.pop()
ans = 1
for _ in range(N - 1):
    std = stk.pop()
    if std > right:
        ans += 1
        right = std
print(ans)
