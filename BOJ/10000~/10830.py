import sys


def mul(B):
    if B == 1:
        return matrix
    tmp = mul(B // 2)
    if B % 2:
        return [[sum((a * b) % 1000 for a, b in zip(A_row, B_col)) % 1000 for B_col in zip(*matrix)] for A_row in [[sum((a * b) % 1000 for a, b in zip(A_row, B_col)) % 1000 for B_col in zip(*tmp)] for A_row in tmp]]
    else:
        return [[sum((a * b) % 1000 for a, b in zip(A_row, B_col)) % 1000 for B_col in zip(*tmp)] for A_row in tmp]


N, B = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append([i % 1000 for i in tmp])
ans = mul(B)
for a in ans:
    a = [str(i) for i in a]
    print(' '.join(a))
