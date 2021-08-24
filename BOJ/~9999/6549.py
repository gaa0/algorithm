import sys


def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    pl = mid
    pr = mid + 1
    result = 0
    height = min(A[pl], A[pr])
    while low <= pl and pr < high + 1:
        width = pr - pl + 1
        if height * width > result:
            result = height * width
        if pl == low and pr == high:
            return result
        if pl == low:
            pr += 1
            if A[pr] < height:
                height = A[pr]
        elif pr == high:
            pl -= 1
            if A[pl] < height:
                height = A[pl]
        elif A[pl - 1] >= A[pr + 1]:
            pl -= 1
            if A[pl] < height:
                height = A[pl]
        elif A[pl - 1] < A[pr + 1]:
            pr += 1
            if A[pr] < height:
                height = A[pr]
    return result


def FIND_MAXIMUM_SUBARRAY(A, low, high):
    if low == high:
        return A[low]
    else:
        mid = (low + high) // 2
        left_max = FIND_MAXIMUM_SUBARRAY(A, low, mid)
        right_max = FIND_MAXIMUM_SUBARRAY(A, mid + 1, high)
        cross_max = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
        return max(left_max, right_max, cross_max)


while 1:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n = data[0]
    case = data[1:]
    print(FIND_MAXIMUM_SUBARRAY(case, 0, n - 1))
