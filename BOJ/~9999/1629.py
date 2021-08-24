import sys

def mul(A, B, C):
    if B <= 2:
        return A ** B % C
    if B % 2:  # 홀수
        return mul(A, B // 2, C) ** 2 * A % C
    else:  # 짝수
        return mul(A, B // 2, C) ** 2 % C

A, B, C = map(int, sys.stdin.readline().split())
print(mul(A, B, C))