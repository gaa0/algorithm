import sys

sys.stdin = open('input.txt')

data = input()
ans = '('
num = ''
for i in range(len(data)):
    if data[i] not in ['-', '+']:
        num += data[i]
    else:
        ans += str(int(num))
        num = ''
        if data[i] == '-':
            ans += ')-('
        else:
            ans += '+'
        continue
    if i == len(data) - 1:
        ans += str(int(num))
        ans += ')'
print(eval(ans))
