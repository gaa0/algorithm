import sys

N, K = map(int, sys.stdin.readline().split())
M = N - K
n = input()
n_list = [int(i) for i in n]
stk = []
for num in n_list:
    while stk:
        if K == 0:
            break
        x = stk.pop()
        if x < num:
            K -= 1
        else:
            stk.append(x)
            break
    if len(stk) < M:
        stk.append(num)
stk = [str(i) for i in stk]
print(''.join(stk))
