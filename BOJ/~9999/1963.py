import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    prime = [0] * 10000
    for i in range(2, 101):
        for j in range(i + i, 10000, i):
            prime[j] = 1
    org, next_num = map(str, sys.stdin.readline().split())
    q = deque([[s for s in org] + [0]])
    ans = [s for s in next_num]
    prime[int(''.join(org))] = 2
    flag = 0

    while q:
        num = q.popleft()
        if num[:4] == ans:
            print(num[-1])
            flag = 1
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    pass
                else:
                    copy_num = num[:]
                    if i != 4:
                        copy_num[i] = str(j)
                        if prime[int(''.join(copy_num[:4]))] == 0:
                            prime[int(''.join(copy_num[:4]))] = 2
                            q.append(copy_num[:4] + [num[-1] + 1])
    if flag == 0:
        print('Impossible')
