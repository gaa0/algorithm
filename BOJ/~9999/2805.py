import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    trees = sorted(list(map(int, sys.stdin.readline().split())))
    max_tree = trees[-1]

    pl = 0
    pr = max_tree - 1
    ans_list = []
    while True:
        pc = (pl + pr) // 2
        sum_high = 0
        for tree in trees:
            if tree > pc:
                sum_high += tree - pc
        if sum_high == M:
            ans_list.append(pc)
            break
        elif sum_high > M:
            ans_list.append(pc)
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break

    print(max(ans_list))

main()