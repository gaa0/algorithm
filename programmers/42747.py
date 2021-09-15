def solution(citations):
    N = len(citations)
    answer = 0
    for i in range(N, 0, -1):
        cnt = 0
        for j in range(N):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i >= N - cnt and i > answer:
            answer = i
    return answer


citations = [3, 0, 6, 1, 5]
citations.sort(reverse=True)
print(list(map(min, enumerate(citations, start=1))))

