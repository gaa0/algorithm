import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
N_cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_cards = list(map(int, sys.stdin.readline().split()))
for n in M_cards:
    if n in N_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
