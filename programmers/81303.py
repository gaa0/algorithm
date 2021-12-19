import heapq


def solution(n, k, cmd):
    answer = ''
    before_cursor = [(-i, i) for i in range(k + 1)]
    heapq.heapify(before_cursor)
    after_cursor = [i for i in range(k + 1, n)]
    heapq.heapify(after_cursor)
    del_list = []
    for cmdOne in cmd:
        if cmdOne[0] == 'D':
            for _ in range(int(cmdOne.split()[-1])):
                num = heapq.heappop(after_cursor)
                heapq.heappush(before_cursor, (-num, num))
        elif cmdOne[0] == 'C':
            del_list.append(heapq.heappop(before_cursor)[1])
            if len(after_cursor) != 0:
                num = heapq.heappop(after_cursor)
                heapq.heappush(before_cursor, (-num, num))
        elif cmdOne[0] == 'U':
            for _ in range(int(cmdOne.split()[-1])):
                heapq.heappush(after_cursor, heapq.heappop(before_cursor)[1])
        else:
            del_row = del_list.pop()
            if del_row < before_cursor[0][1]:
                heapq.heappush(before_cursor, (-del_row, del_row))
            else:
                heapq.heappush(after_cursor, del_row)
    ans = set([i[1] for i in before_cursor] + after_cursor)
    for i in range(n):
        if i in ans:
            answer += 'O'
        else:
            answer += 'X'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))
