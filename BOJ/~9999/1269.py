A_N, B_N = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

ans_set = set()

for i in A_set:
    if i not in B_set:
        ans_set.add(i)
for i in B_set:
    if i not in A_set:
        ans_set.add(i)
        
print(len(ans_set))