A = int(input())
B = int(input())
C = int(input())

g = [0] * 10
a = str(A * B * C)
for i in a:
    g[int(i)] += 1

for gg in g:
    print(gg)
