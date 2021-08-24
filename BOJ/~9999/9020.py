import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    r = int(n // 2 + 1) if n % 2 else int(n / 2)
    for i in range(r, n):
        chk1 = 0
        for j in range(2, i):
            if i % j == 0:
                chk1 = 1
                break
        if chk1 == 1:
            continue
        n_prime = n - i
        chk2 = 0
        for j in range(2, n_prime):
            if n_prime % j == 0:
                chk2 = 1
                break
        if chk2 == 1:
            continue
        print(n_prime, i)
        break
