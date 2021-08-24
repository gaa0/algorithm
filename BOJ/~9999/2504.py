import sys

data = input()
stk = []
tmp = None
chk = 0
for s in data:
    if s == '(':
        stk.append((2, 'L'))
    elif s == '[':
        stk.append((3, 'L'))
    elif s == ')':
        if not stk:
            break
        x = stk[-1]
        if x == (3, 'L'):
            break
        if x == (2, 'L'):
            stk.pop()
            if len(stk) > 1 and stk[-1][1] == 'C':
                stk[-1][0] += 2
            else:
                stk.append([2, 'C'])
        elif len(stk) >= 2 and x[1] == 'C' and stk[-2] == (2, 'L'):
            y = stk.pop()
            stk.pop()
            stk.append([y[0] * 2, 'C'])
            if len(stk) > 2 and stk[-2][1] == 'C':
                tmp_c = stk.pop()
                stk[-1][0] += tmp_c[0]
        else:
            chk = 1
            break
    elif s == ']':
        if not stk:
            break
        tmp = stk[-1]
        if tmp == (2, 'L'):
            break
        if tmp == (3, 'L'):
            stk.pop()
            if len(stk) > 1 and stk[-1][1] == 'C':
                stk[-1][0] += 3
            else:
                stk.append([3, 'C'])
        elif len(stk) >= 2 and tmp[1] == 'C' and stk[-2] == (3, 'L'):
            y = stk.pop()
            stk.pop()
            stk.append([y[0] * 3, 'C'])
            if len(stk) > 2 and stk[-2][1] == 'C':
                tmp_c = stk.pop()
                stk[-1][0] += tmp_c[0]
        else:
            chk = 1
            break
ans = 0
if chk != 1:
    for c in stk:
        ans += c[0]
        if c[1] != 'C':
            ans = 0
            break
print(ans)
