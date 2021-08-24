import sys

# 링 버퍼로 안 하면 시간 초과
N = int(sys.stdin.readline())
que = [None] * 2000000
no = 0
front = 0
rear = 0
capacity = 0
for _ in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        que[rear] = data[1]
        rear += 1
        no += 1
    elif data[0] == 'pop':
        if no > 0:
            x = que[front]
            front += 1
            no -= 1
            print(x)
        else:
            print(-1)
    elif data[0] == 'size':
        print(no)
    elif data[0] == 'empty':
        chk = 1
        for i in range(no):
            idx = (i + front)
            if que[idx]:
                chk = 0
                break
        print(chk)
    elif data[0] == 'front':
        if no > 0:
            print(que[front])
        else:
            print(-1)
    else:
        if no > 0:
            print(que[rear - 1])
        else:
            print(-1)
