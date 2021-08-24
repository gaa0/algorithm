import sys

A, B, V = map(int, sys.stdin.readline().split())

a = A - B
v_a = V - A
if v_a % a:
    answer = v_a // a + 2
else:
    answer = v_a // a + 1

print(answer)
