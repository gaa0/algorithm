import sys

sys.stdin = open('input.txt')

first_str = input()
explosion_str = input()

ans = ''
for s in first_str:
    if s not in explosion_str:
        ans += s

if ans == '':
    ans = 'FRULA'

print(ans)
