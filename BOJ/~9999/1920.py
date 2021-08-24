import sys

def bin_search(a, key):
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    idx = bin_search(N_list, m)
    print(idx)