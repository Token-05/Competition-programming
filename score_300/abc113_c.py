# この方法では間に合わない

# N, M = map(int, input().split())
# citylist = [list(map(int, input().split())) for _ in range(M)]
# manlist = []

# for i in range(1,N+1):
#     for city in citylist:
#         if city[0] == i:
#             manlist.append(city[1])
#     manlist.sort()
#     for j in citylist:
#         if j[0] == i:
#             j.append(str(j[0]).zfill(6) + str(manlist.index(j[1])+1).zfill(6))
#     manlist.clear()

# for city in citylist:
#     print(city[2])

# こちらで間に合う

N, M = map(int, input().split())
py = [[] for _ in range(N)]
for i in range(M):
    j, y = map(int, input().split())
    py[j-1].append((y, i))
for i in range(N):
    py[i].sort()
result = [0]*M

for j in range(N):
    # インデックス番号, 要素の順に取得
    for x, (_, i) in enumerate(py[j]):
        result[i] = str(j+1).zfill(6) + str(x+1).zfill(6)

for i in range(M):
    print(result[i])