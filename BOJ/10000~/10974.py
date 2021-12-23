import sys
from itertools import permutations

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
num_list = list(range(1, N + 1))
per_list = list(permutations(num_list, N))
for per in per_list:
    print(*per)
