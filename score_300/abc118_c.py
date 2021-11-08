N = int(input())
A = list(map(int, input().split()))

while True:
    minsize = min(A)
    index = A.index(minsize)
    A = list(map(lambda x: x%minsize, A))
    A[index] = minsize
    A = [i for i in A if i != 0]
    if len(A) == 1:
        break

print(max(A))