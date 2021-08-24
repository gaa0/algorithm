garo, sero = map(int, input().split())
n = int(input())
garo_list = [0, garo]
sero_list = [0, sero]
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0]:
        garo_list.append(data[1])
    else:
        sero_list.append(data[1])
garo_list.sort(reverse=True)
sero_list.sort(reverse=True)
garo_len_list = []
sero_len_list = []
for i in range(len(garo_list) - 1):
    garo_len_list.append(garo_list[i] - garo_list[i + 1])
for i in range(len(sero_list) - 1):
    sero_len_list.append(sero_list[i] - sero_list[i + 1])
ans = 0
for g in garo_len_list:
    for s in sero_len_list:
        area = g * s
        if area > ans:
            ans = area

print(ans)
