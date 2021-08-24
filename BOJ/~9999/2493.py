import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
top_list = []
for i in range(N):
    top_list.append((i, top[i]))

stk = []
ans = [0] * N
for i in range(N):
    if stk:
        for j in range(len(stk) - 1, -1, -1):
            x = stk[j]
            if x[1] > top[i]:
                ans[i] = x[0] + 1
                break
            else:
                stk.pop()
    stk.append(top_list[i])
ans = [str(i) for i in ans]
print(' '.join(ans))
