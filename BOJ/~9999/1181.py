import sys

N = int(sys.stdin.readline())
x = [[] for _ in range(51)]

for _ in range(N):
    word = input()
    tmp = x[len(word)]
    if word not in tmp:
        tmp.append(word)
for i in range(51):
    if x[i]:
        x[i].sort()
        for ans in x[i]:
            print(ans)