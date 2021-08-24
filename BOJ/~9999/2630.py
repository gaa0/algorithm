import sys

def make(a, N):
    global white, blue
    if N == 1:
        for last_quater in a:
            if last_quater == [0]:
                white += 1
                return
            elif last_quater == [1]:
                blue += 1
                return
    quaters = [[] for _ in range(4)]
    quaters_sum = [0] * 4
    half_N = int(N / 2)
    for i in range(N):
        if i < half_N:
            first_quater = a[i][:half_N]
            quaters[0].append(first_quater)
            quaters_sum[0] += sum(first_quater)
            second_quater = a[i][half_N:]
            quaters[1].append(second_quater)
            quaters_sum[1] += sum(second_quater)
        else:
            third_quater = a[i][:half_N]
            quaters[2].append(third_quater)
            quaters_sum[2] += sum(third_quater)
            fourth_quater = a[i][half_N:]
            quaters[3].append(fourth_quater)
            quaters_sum[3] += sum(fourth_quater)
    for i in range(4):
        if quaters_sum[i] == 0:
            white += 1
            continue
        elif quaters_sum[i] == half_N ** 2:
            blue += 1
            continue
        else:
            make(quaters[i], int(half_N))

N = int(sys.stdin.readline())
data = []
sum_data = 0
for _ in range(N):
    tmp_data = list(map(int, sys.stdin.readline().split()))
    data.append(tmp_data)
    sum_data += sum(tmp_data)
white = 0
blue = 0
if sum_data == 0:
    white += 1
elif sum_data == N ** 2:
    blue += 1
else:
    make(data, N)

print(white)
print(blue)