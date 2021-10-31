S = list(input())
T = list(input())
N = len(S)
combinations = []
onlyone = [[],[]]

for i in range(N):
    com = list([S[i],T[i]])
    if com not in combinations:
        combinations.append(com)
        onlyone[0].append(S[i])
        onlyone[1].append(T[i])

for j in onlyone[0]:
    if onlyone[0].count(j) > 1:
        print("No")
        exit(0)

for j in onlyone[1]:
    if onlyone[1].count(j) > 1:
        print("No")
        exit(0)

print("Yes")