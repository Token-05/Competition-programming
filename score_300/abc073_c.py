N = int(input())
A = list(input() for i in range(N))

memo = {}
result = {}
for i in A:
    if i in memo.keys():
        memo[i] += 1
    else:
        memo[i] = 1

for i,j in memo.items():
    if j % 2 == 1:
        result[i] = j

print(len(result))