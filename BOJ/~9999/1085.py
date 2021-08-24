x, y, w, h = map(int, input().split())

s = {x, y, w - x, h - y}

print(min(s))
