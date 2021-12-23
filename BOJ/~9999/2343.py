import sys

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
lec_list = list(map(int, sys.stdin.readline().split()))

pl = max(lec_list)
pr = sum(lec_list)
ans = pr
while pl < pr:
    mid = (pl + pr) // 2
    temp_sum = 0
    temp_ans = 1
    chk = 0
    for i in lec_list:
        if temp_sum + i <= mid:
            temp_sum += i
        else:
            temp_ans += 1
            temp_sum = i
            if temp_ans > M:
                chk = 1
                pl = mid + 1
                break
    if chk == 1:
        continue
    ans = min(mid, ans)
    pr = mid
print(ans)
