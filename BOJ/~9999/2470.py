import sys

N = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().split())))
pl = 0
pr = N - 1
min_sum = [2000000000, None, None]
while pl < pr:
    x = data[pl] + data[pr]
    if x == 0:
        min_sum[1] = data[pl]
        min_sum[2] = data[pr]
        break
    elif abs(x) < min_sum[0]:
        min_sum[0] = abs(x)
        min_sum[1] = data[pl]
        min_sum[2] = data[pr]
    if x < 0:
        pl += 1
    else:
        pr -= 1
min_sum = [str(i) for i in min_sum[1:]]
print(' '.join(min_sum))
