import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
num = [int(i) for i in input()]
answer = []

for n in num:
    while K and answer and answer[-1] < n:
        answer.pop()
        K -= 1
    answer.append(n)

if K > 0:
    answer = answer[:len(answer) - K]

ans = ''
for i in answer:
    ans += str(i)
print(ans)
