import sys
from itertools import combinations

x = []

for _ in range(9):
    x.append(int(sys.stdin.readline()))

c = list(combinations(x, 2))

for two in c:
    if sum(x) - two[0] - two[1] == 100:
        x.remove(two[0])
        x.remove(two[1])
        x.sort()
        for nan in x:
            print(nan)
        break
