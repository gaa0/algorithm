import sys

N = int(sys.stdin.readline())
cards = list(range(1, N + 1))
front = 0
rear = 0
no = N
while no > 1:
    front += 1
    no -= 1
    if no > 1:
        x = cards[front]
        front += 1
        cards.append(x)
print(cards[front])
