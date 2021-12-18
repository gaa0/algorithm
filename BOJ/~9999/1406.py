import sys
from collections import deque

sys.stdin = open('input.txt')

before_cursor = deque([i for i in input()])
T = int(sys.stdin.readline())
after_cursor = deque()
for _ in range(T):
    instruction = input()
    if instruction[0] == 'P':
        before_cursor.append(instruction[-1])
    elif instruction[0] == 'L' and len(before_cursor) != 0:
        deque.insert(after_cursor, 0, before_cursor.pop())
    elif instruction[0] == 'D' and len(after_cursor) != 0:
        before_cursor.append(deque.popleft(after_cursor))
    elif instruction[0] == 'B' and len(before_cursor) != 0:
        before_cursor.pop()
print(''.join(before_cursor + after_cursor))
