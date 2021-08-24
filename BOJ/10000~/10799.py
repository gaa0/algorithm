import sys

data = input()
stk = []
bar = 0
ans = 0
chk = 0
for i in range(len(data)):
    if data[i] == '(':
        stk.append(data[i])
        bar += 1
    else:
        x = stk[-1]
        if x == '(':
            if chk == 1:
                ans += 1
                bar -= 1
                stk.pop()
                if i < len(data) - 1 and data[i + 1] != ')':
                    chk = 0
            else:
                bar -= 1
                stk.pop()
                stk.append('0')
                if len(stk) >= 2 and stk[-2] == '0':
                    stk.pop()
                ans += bar
        else:
            chk = 1
            ans += 1
            bar -= 1
            stk.pop()
            stk.pop()
            if i < len(data) - 1 and data[i + 1] != ')':
                chk = 0
print(ans)
