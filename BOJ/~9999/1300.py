import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

pl = 1
pr = k
ans = 0
while pl <= pr:
    mid = (pl + pr) // 2
    temp_sum = 0
    for i in range(1, N + 1):
        temp_sum += min(mid // i, N)
    if temp_sum >= k:
        ans = mid
        pr = mid - 1
    else:
        pl = mid + 1
print(ans)
