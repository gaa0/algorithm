words = [input(), input()]
word = '$'.join(words)
word_len = len(word)

sa = [i for i in range(word_len)]
rank = [ord(i) for i in word]
tmp = [0] * word_len


def f(x): return rank[x] if x < word_len else -1


t = 1
while 1:
    sa.sort(key=lambda x: (f(x), f(x + t)))
    r = 0
    tmp[sa[0]] = 0
    for i in range(1, word_len):
        if f(sa[i - 1]) != f(sa[i]) or f(sa[i - 1] + t) != f(sa[i] + t):
            r += 1
        tmp[sa[i]] = r
    rank = tmp[:]
    if r == word_len - 1:
        break
    t <<= 1

LCP = [0] * word_len
length = 0
for i in range(word_len):
    length = max(length - 1, 0)
    if rank[i] + 1 == word_len:
        continue
    j = sa[rank[i] + 1]
    while 1:
        if i + length < word_len and j + length < word_len and word[i + length] == word[j + length]:
            length += 1
        else:
            break
    LCP[rank[i]] = length

ans = (0, 0)
for i, v in enumerate(LCP):
    if i != word_len - 1:
        if sa[i] < len(words[0]) < sa[i + 1] or sa[i + 1] < len(words[0]) < sa[i]:
            ans = max(ans, (v, i))

print(ans[0])
s = sa[ans[1]]
print(word[s:s + ans[0]])
