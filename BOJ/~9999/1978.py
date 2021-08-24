import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

answer = 0
for d in data:
    if d > 1:
        answer += 1
        for i in range(2, d):
            if d % i == 0:
                answer -= 1
                break

print(answer)
