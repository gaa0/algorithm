bf_list = []


def col_chk(x, y):
    if [x, y - 1, 0] in bf_list or [x - 1, y, 1] in bf_list or [x, y, 1] in bf_list:
        return True
    return False


def beam_chk(x, y):
    if [x, y - 1, 0] in bf_list or [x + 1, y - 1, 0] in bf_list or ([x - 1, y, 1] in bf_list and [x + 1, y, 1] in bf_list):
        return True
    return False


def solution(n, build_frame):
    for x, y, a, b in build_frame:
        if a == 0:  # 기둥
            if b == 1:  # 설치
                if y == 0 or col_chk(x, y):
                    bf_list.append([x, y, a])
            else:  # 삭제
                bf_list.remove([x, y, 0])
                chk = 1
                if [x, y + 1, 0] in bf_list:  # 삭제하려는 기둥 위의 기둥
                    if not col_chk(x, y + 1):
                        chk = 0
                if [x - 1, y + 1, 1] in bf_list:
                    if not beam_chk(x - 1, y + 1):
                        chk = 0
                if [x, y + 1, 1] in bf_list:
                    if not beam_chk(x - 1, y + 1):
                        chk = 0
                if chk == 0:
                    bf_list.append([x, y, 0])

        else:  # 보
            if b == 1:  # 설치
                if beam_chk(x, y):
                    bf_list.append([x, y, a])
            else:  # 삭제
                bf_list.remove([x, y, 1])
                chk = 1
                if [x, y, 0] in bf_list:
                    if not col_chk(x, y):
                        chk = 0
                if [x + 1, y, 0] in bf_list:
                    if not col_chk(x + 1, y):
                        chk = 0
                if [x - 1, y, 1] in bf_list:
                    if not beam_chk(x - 1, y):
                        chk = 0
                if [x + 1, y, 1] in bf_list:
                    if not beam_chk(x + 1, y):
                        chk = 0
                if chk == 0:
                    bf_list.append([x, y, 1])
    bf_set = sorted(bf_list)
    return bf_set


n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
