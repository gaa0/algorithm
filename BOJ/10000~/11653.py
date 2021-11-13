import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

prime = [True] * (N + 1)
m = int(N ** 0.5)
for i in range(2, m + 1):
    if prime[i]:
        for j in range(i + i, N, i):
            prime[j] = False

prime_number = [i for i in range(2, N + 1) if prime[i]]
# print(prime_number)

while N != 1:
    for i in prime_number:
        if N % i == 0:
            print(i)
            N //= i
            break
