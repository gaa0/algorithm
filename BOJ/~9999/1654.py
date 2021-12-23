import sys

sys.stdin = open('input.txt')

K, N = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]

pl = 1
pr = sum(lan_list) // N
ans = 0
mid_set = set()
while pl <= pr:
    mid = (pl + pr) // 2
    if mid in mid_set:
        break
    else:
        mid_set.add(mid)
    temp_ans = 0
    for lan in lan_list:
        temp_ans += lan // mid
    if temp_ans >= N:
        ans = max(mid, ans)
        pl = mid + 1
    else:
        pr = mid
print(ans)
