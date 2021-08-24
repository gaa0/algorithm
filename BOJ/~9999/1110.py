def cul(num):
    global cnt, N
    if int(num) == int(N) and cnt:
        return
    if len(num) == 1:
        num = num + '0'
    n1 = int(num[0]) + int(num[1])
    new = str(int(num[1])) + str(n1 % 10)
    cnt += 1
    cul(new)

N = input()

if len(N) == 1:
    N = N + '0'
cnt = 0
cul(N)
print(cnt)