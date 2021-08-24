import sys

T = int(sys.stdin.readline())
for t in range(T):
    stk = []
    data = input()
    chk = 1
    for d in data:
        if d == '(':
            stk.append(d)
        else:
            if stk:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    print('NO')
                    chk = 0
                    break
            else:
                print('NO')
                chk = 0
                break
    if chk == 1 and len(stk) == 0:
        print('YES')
    elif chk == 0:
        pass
    else:
        print('NO')