import sys

N = int(sys.stdin.readline())
stk = []
for _ in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        stk.append(int(data[1]))
    elif data[0] == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif data[0] == 'size':
        print(len(stk))
    elif data[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)
