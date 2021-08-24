import sys

N = sys.stdin.readline()
if len(N) <= 3:
    ans = int(N)
else:
    N = int(N)
    ans = 99
    for i in range(111, N + 1):
        a = i // 100 - i // 10 % 10
        b = i // 10 % 10 - i % 10
        if a == b:
            ans += 1
print(ans)
