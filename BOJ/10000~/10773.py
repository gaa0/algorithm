import sys

stk = []
K = int(sys.stdin.readline())
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))