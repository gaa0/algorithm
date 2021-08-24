import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

c = list(permutations(arr, N))

ans = 0
for tmp_list in c:
    tmp = 0
    for i in range(N - 1):
        tmp += abs(tmp_list[i] - tmp_list[i + 1])
    if tmp > ans:
        ans = tmp

print(ans)
