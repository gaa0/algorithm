import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
multi = [0] * N
ans = 0
for i in range(K):
    if data[i] in multi:
        continue
    else:
        if 0 in multi:
            multi[multi.index(0)] = data[i]
        else:
            last = 0
            for j in multi:
                chk = 0
                for k in range(i + 1, K):
                    if j == data[k]:
                        chk = 1
                        if k > last:
                            last = k
                            break
                        else:
                            break
                if chk == 0:
                    last = data.index(j)
                    break
            multi[multi.index(data[last])] = data[i]
            ans += 1
print(ans)
