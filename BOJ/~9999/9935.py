import sys

sys.stdin = open('input.txt')

first_str = input()
explosion_str = list(map(str, input()))
str_N = len(first_str)
N = len(explosion_str)

ans = []

i = 0
while i < str_N:
    ans.append(first_str[i])
    if len(ans) >= N and ans[-N:] == explosion_str:
        for _ in range(N):
            ans.pop()
    i += 1

if ans:
    print(''.join(ans))
else:
    print('FRULA')
