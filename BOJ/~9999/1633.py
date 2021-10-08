import sys

sys.stdin = open('input.txt')

player_list = []
for line in sys.stdin:
    player_list.append([int(i) for i in line.split()])

dp = [[0] * 16 for _ in range(16)]

for white, black in player_list:
    for w in range(15, -1, -1):
        for b in range(15, -1, -1):
            if w - 1 < 0 and b - 1 < 0:
                continue
            elif w - 1 < 0:
                dp[w][b] = max(dp[w][b - 1] + black, dp[w][b])
            elif b - 1 < 0:
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b])
            else:
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b - 1] + black, dp[w][b])

print(dp[15][15])
