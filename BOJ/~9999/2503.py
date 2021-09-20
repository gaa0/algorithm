import sys
from itertools import permutations

sys.stdin = open('3_input.txt')

num_list = list(range(1, 10))
per_list = list(permutations(num_list, 3))
N = int(sys.stdin.readline())
for _ in range(N):
    q, s, b = sys.stdin.readline().split()
    s, b = int(s), int(b)
    tmp_list = []
    for per in per_list:
        s_chk = 0
        b_chk = 0
        for i in range(3):
            if per[i] == int(q[i]):
                s_chk += 1
            if str(per[i]) in q:
                b_chk += 1
        if s_chk == s and b_chk - s_chk == b:
            tmp_list.append(per)
    per_list = tmp_list
print(len(per_list))
