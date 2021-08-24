T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    N = data.pop(0)
    avg = sum(data) / N
    cnt = 0
    for d in data:
        if d > avg:
            cnt += 1
    print(format(cnt / N * 100, ".3f") + '%')