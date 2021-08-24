import sys


def FIND_MIN_CROSSING_SUBARRAY(low, mid, high, std):
    real_point = []
    mid_point = A[mid]
    mid_point_x, mid_point_y = mid_point[0], mid_point[1]
    for p in A[low:high + 1]:
        if (p[0] - mid_point_x) ** 2 <= std:
            real_point.append(p)
    real_point.sort(key=lambda x: x[1])
    for i in range(len(real_point) - 1):
        for j in range(i + 1, len(real_point)):
            if (real_point[i][1] - real_point[j][1]) ** 2 >= std:
                break
            d = (real_point[i][0] - real_point[j][0]) ** 2 + (
                        real_point[i][1] - real_point[j][1]) ** 2
            if d < std:
                std = d
    return std


def FIND_MINIMUM_SUBARRAY(low, high):
    if high - low <= 2:
        short = float('inf')
        for i in range(low, high):
            for j in range(i + 1, high + 1):
                d = (A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2
                if d < short:
                    short = d
        return short
    else:
        mid = (low + high) // 2
        left_min = FIND_MINIMUM_SUBARRAY(low, mid)
        right_min = FIND_MINIMUM_SUBARRAY(mid + 1, high)
        cross_min = FIND_MIN_CROSSING_SUBARRAY(low, mid, high, min(left_min, right_min))
        return min(left_min, right_min, cross_min)


n = int(sys.stdin.readline())
A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

A = sorted(list(set(A)))
if n != len(A):
    print(0)
else:
    print(FIND_MINIMUM_SUBARRAY(0, n - 1))
