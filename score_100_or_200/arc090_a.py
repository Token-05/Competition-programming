N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
max = []
for i in range(N):
    max.append(sum(A1[:i+1]) + sum(A2[i:]))
    max.sort(reverse=True)
print(max[0])