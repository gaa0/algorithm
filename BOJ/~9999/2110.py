import sys

def main():
    N, C = map(int, sys.stdin.readline().split())
    home_list = []
    for _ in range(N):
        home_list.append(int(sys.stdin.readline()))
    home_list.sort()
    if N == 2:
        ans = (home_list[-1] - home_list[0])
    else:
        pl = 1
        pr = (home_list[-1] - home_list[0])

        pc_list = set()
        while pl <= pr:
            pc = (pl + pr) // 2
            cnt = 1
            i = 0
            j = 1
            # chk = 1
            # min_pc = set()
            while cnt < C:
                if home_list[j] - home_list[i] >= pc:
                    cnt += 1
                    # min_pc.add(home_list[j] - home_list[i])
                    i = j
                if cnt == C:
                    # chk = 2
                    pc_list.add(pc)
                    pl = pc + 1
                    break
                elif home_list[-1] - home_list[i] < pc:
                    # chk = 0
                    pr = pc - 1
                    break
                j += 1
                if j >= N:
                    break
            # if chk == 2:
                # pl = max(pc_list) + 1
                # pl = pc + 1
            # elif chk == 0:
            #     pr = pc - 1
        ans = max(pc_list)
    print(ans)
main()