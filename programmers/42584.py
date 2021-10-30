def solution(prices):
    N = len(prices)
    answer = [0] * N
    for i in range(N - 1):
        for j in range(i + 1, N):
            answer[i] += 1
            if prices[j] < prices[i]:
                break

    return answer
