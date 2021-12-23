import sys
from itertools import combinations

sys.stdin = open('input.txt')

while 1:
    data = list(map(int, sys.stdin.readline().split()))
    if data == [0]:
        break
    k = data[0]
    nums = data[1:]
    com_list = list(combinations(nums, 6))
    for com in com_list:
        print(*com)
    print()
