# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = set(A)
    for i in range(1, 1000002):
        if i not in A:
            return i