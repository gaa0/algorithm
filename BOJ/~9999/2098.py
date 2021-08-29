import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)


def tsp(N, costs):
    dp = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == (1 << N) - 1:
            return costs[last][0] or INF

        if dp[last][visited]:
            return dp[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and costs[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + costs[last][city])
        dp[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)


N = int(sys.stdin.readline())
costs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(tsp(N, costs))
