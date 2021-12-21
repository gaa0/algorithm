import sys

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            temp = cards[i] + cards[j] + cards[k]
            if M >= temp > ans:
                ans = temp

print(ans)
