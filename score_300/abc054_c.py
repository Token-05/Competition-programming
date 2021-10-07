#全探索
from itertools import permutations
N, M = map(int, input().split())
AB = [input() for _ in range(M)]
l = [str(i) for i in range(1, N + 1)]
perm = list(permutations(l, N))
ans = 0
for i in perm:
    i = list(i)
    flag = False
    if i[0] != "1":break
    for j in range(len(i)):
        if j == len(i) - 1:
            flag = True
            break
        a = f"{i[j]} {i[j + 1]}"
        b = f"{i[j + 1]} {i[j]}"
        if a not in AB and b not in AB:
            break
    if flag: ans += 1
print(ans)