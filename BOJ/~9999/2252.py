import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
indegree = [0] * (N + 1)  # 모든 노드에 대한 진입차수의 초기값은 0

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)  # 정점 a에서 b로 이동 가능
    indegree[b] += 1  # 진입차수 1 증가


def topology_sort():  # 위상 정렬 함수
    result = []
    q = deque()
    for i in range(1, N + 1):  # 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
    while q:  # 큐가 빌 때까지 반복
        now = q.popleft()
        result.append(now)
        for i in G[now]:  # 꺼낸 원소와 연결된 노드들의 진입차수 - 1
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
