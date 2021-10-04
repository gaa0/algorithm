from collections import defaultdict


def solution(gems):
    answer = [0, 0]
    gem_len, gem_kind = len(gems), len(set(gems))
    start, end = 0, 0
    gem_dict = defaultdict(int)
    candidates = []

    while 1:
        kind = len(gem_dict)
        if start == gem_len:
            break
        if gem_kind == kind:
            candidates.append((start, end))
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
            continue
        if end == gem_len:
            break
        if gem_kind != kind:
            gem_dict[gems[end]] += 1
            end += 1

    min_len = float('inf')
    for s, e in candidates:
        tmp_len = e - s
        if tmp_len < min_len:
            min_len = tmp_len
            answer[0] = s + 1
            answer[1] = e
    return answer


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
