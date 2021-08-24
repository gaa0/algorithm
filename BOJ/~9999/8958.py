T = int(input())

for _ in range(T):
    a = input()
    ans = 0
    chk = 0
    for i in range(len(a)):
        if a[i] == 'O':
            chk += 1
            ans += chk
        else:
            chk = 0
    print(ans)