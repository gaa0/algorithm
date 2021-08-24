N, X = map(int, input().split())
A = list(map(int, input().split()))

ans_list = []

for i in A:
    if i < X:
        ans_list.append(str(i))

print(' '.join(ans_list))
