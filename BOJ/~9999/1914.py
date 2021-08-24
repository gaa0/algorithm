import sys

sys.setrecursionlimit(10 ** 8)


def move(no, x, y):
    global ans
    if no > 1:
        ans += 1
        move(no - 1, x, 6 - x - y)
    answer.append(f'{x} {y}')
    if no > 1:
        ans += 1
        move(no - 1, 6 - x - y, y)


N = int(sys.stdin.readline())
if N <= 20:
    ans = 1
    answer = []
    move(N, 1, 3)
    print(ans)
    for a in answer:
        print(a)
else:
    print(2 ** N - 1)