# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    cnt = 0
    ans = 0
    for s in str(bin(N)[2:]):
        if s == '1':
            ans = max(ans, cnt)
            cnt = 0
        else:
            cnt += 1
    return ans
