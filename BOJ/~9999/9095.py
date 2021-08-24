import sys

def two(two_list):
    chk = 0
    for i in range(len(two_list) - 1):
        two_list_copy = [i for i in two_list]
        if two_list_copy[i] == 1 and two_list_copy[i + 1] == 1:
            two_list_copy[i] = 2
            del two_list_copy[i + 1]
            if two_list_copy not in ans_list:
                chk = 1
                ans_list.append(two_list_copy)
                two(two_list_copy)
    if chk == 0:
        return

def three(t_f_t):
    chk = 0
    for i in range(len(t_f_t) - 1):
        t_f_t_copy = [i for i in t_f_t]
        if t_f_t_copy[i] + t_f_t_copy[i + 1] == 3:
            t_f_t_copy[i] = 3
            del t_f_t_copy[i + 1]
            if t_f_t_copy not in ans_list:
                chk = 1
                ans_list.append(t_f_t_copy)
                three([t_f_t_copy])
    if chk == 0:
        return

T = int(sys.stdin.readline())
for _ in range(T):
    ans_list = []
    n = int(sys.stdin.readline())
    sum_list = [1] * n
    ans_list.append(sum_list)
    two(sum_list)
    for two_for_three in ans_list:
        three(two_for_three)
    print(len(ans_list))