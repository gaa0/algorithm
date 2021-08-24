import sys

N, r, c = map(int, sys.stdin.readline().split())

side_len = 2 ** N  # 8
half_side_len = int(side_len / 2)  # 4
quarter_size = side_len ** 2


def Z(r, c, half_side_len, start_point, quarter_size):
    next_quarter_size = int(quarter_size // 4)
    if quarter_size == 4:
        last = [[start_point, start_point + 1], [start_point + 2, start_point + 3]]
        print(last[r][c])
        return
    if r >= half_side_len and c >= half_side_len:  # 4사분면
        r -= half_side_len  # 3
        c -= half_side_len  # 3
        start_point += next_quarter_size * 3
    elif r >= half_side_len:  # 3사분면
        r -= half_side_len
        start_point += next_quarter_size * 2
    elif c >= half_side_len:  # 2사분면
        c -= half_side_len
        start_point += next_quarter_size
    Z(r, c, int(half_side_len / 2), start_point, next_quarter_size)


Z(r, c, half_side_len, 0, quarter_size)
