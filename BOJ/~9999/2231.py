import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
ans = 0
for i in range(N):
    str_N = str(i)
    len_num = len(str_N)
    result = i
    for j in range(len_num):
        result += int(str_N[j])

    if int(result) == N:
        ans = i
        break
print(ans)
