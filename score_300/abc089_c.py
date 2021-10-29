# 間に合わない(全探索)

# import itertools

# N = int(input())
# C = [input()[:1] for _ in range(N)]
# flag = 0
# sortlist = list(itertools.permutations(['M', 'A', 'R', 'C', 'H'], 3))

# for pair in itertools.combinations(C, 3):
#     if pair in sortlist:
#         flag += 1

# print(flag)

# =============================================================================

import itertools

N = int(input())
C = [input()[:1] for _ in range(N)]
sortlist = ['M', 'A', 'R', 'C', 'H']
P = list(itertools.combinations([0,1,2,3,4], 3))
D = []
res = 0

for i in range(5):
    D.append(C.count(sortlist[i]))

for i in range(10):
    res += D[P[i][0]] * D[P[i][1]] * D[P[i][2]]

print(res)