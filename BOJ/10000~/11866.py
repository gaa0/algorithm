import sys

N, K = map(int, sys.stdin.readline().split())
que = list(map(str, range(1, N + 1)))
i = K - 1
no = N
ans_list = []
while no:
    if i >= no:
        while 1:
            i = i - no
            if i < no:
                break
    ans_list.append(que.pop(i))
    no -= 1
    i += K - 1
print(f'<{", ".join(ans_list)}>')
