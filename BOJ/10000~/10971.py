import sys
from itertools import permutations

def main():
    N = int(sys.stdin.readline())
    cities = list(range(N))
    p = list(permutations(cities, N))
    data = []
    for _ in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))
    ans = 987654321
    for case in p:
        case += (case[0],)
        tmp = 0
        chk = 0
        for i in range(N):
            if data[case[i]][case[i + 1]] == 0 or tmp + data[case[i]][case[i + 1]] > ans:
                chk = 1
                break
            tmp += data[case[i]][case[i + 1]]
        if chk == 0: ans = tmp

    print(ans)
main()