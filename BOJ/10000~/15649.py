import sys
from itertools import permutations

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

answer_list = list(permutations(range(1, N + 1), M))
for answer in answer_list:
    for ans in answer:
        print(ans, end=' ')
    print()
