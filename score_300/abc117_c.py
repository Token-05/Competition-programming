# これも全探索（もちろん間に合わない）

# import itertools
# N, M = map(int, input().split())
# X = list(map(int, input().split()))
# minlist = []

# for lists in [list(e) for e in itertools.product(range(N), repeat=M)]:
#     sep = [[] for _ in range(N)]
#     sum = 0
#     for index, list in enumerate(lists):
#         sep[list].append(X[index])
#     for i in sep:
#         if len(i) > 0:
#             sum += max(i) - min(i)
#     minlist.append(sum)
# print(min(minlist))


# マス間の距離をリストにまとめる
# それらをソートして小さい順にN-Mまでの値を足し上げたものが操作回数となる

N, M = map(int, input().split())
X = list(map(int, input().split()))
sa = []

if N >= M: print(0)
else: 
    X.sort()
    for i in range(1,M): sa.append(X[i] - X[i-1])
    sa.sort()
    print(sum(sa[:M-N]))