import sys

sys.stdin = open('input.txt')

X = sys.stdin.readline()
ans = 0
if len(X) >= 2:
    if X[0:2] == '0x':
        ans = int(X, 16)
    elif X[0] == '0':
        ans = int(X, 8)
    else:
        ans = X
else:
    ans = X

print(ans)
