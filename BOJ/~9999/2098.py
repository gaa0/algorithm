import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]


def tsp(last, visited):
    if visited == (1 << N) - 1:
        if W[last][0]:
            return W[last][0]
        else:
            return float('inf')

    if dp[last][visited]:
        return dp[last][visited]

    min_cost = float('inf')
    for i in range(N):
        if visited & (1 << i) != 1 << i and W[last][i]:
            min_cost = min(min_cost, tsp(i, visited | (1 << i)) + W[last][i])
    dp[last][visited] = min_cost
    return min_cost


ans = tsp(0, 1 << 0)
print(ans)
