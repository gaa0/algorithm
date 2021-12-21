import sys
from itertools import combinations

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
word_list = [set() for _ in range(N)]
ans = 0
if K >= 5:
    for i in range(N):
        temp = set(map(str, input())) - {'a', 'n', 't', 'i', 'c'}
        word_list[i] = temp
    if K == 5:
        for word in word_list:
            if not word:
                ans += 1
    else:
        all_word = set()
        for i in range(N):
            all_word |= word_list[i]
        all_word = list(all_word)
        K = min(K, len(all_word) + 5)
        com_word = list(combinations(all_word, K - 5))
        # for word in word_list:
        for com in com_word:
            temp_ans = 0
            # for com in com_word:
            for word in word_list:
                temp_word = set(word)
                for i in range(K - 5):
                    temp_word.discard(com[i])
                if not temp_word:
                    temp_ans += 1
            ans = max(temp_ans, ans)
print(ans)
