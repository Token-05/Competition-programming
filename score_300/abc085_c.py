import sys

N, Y = list(map(int, input().split()))

for i in range(N+1):
    for j in range(N+1):
        k = N - i - j
        if 10000 * i + 5000 * j + 1000 * k == Y and k >= 0:
            print(i,j,k)
            sys.exit(0)

print('-1 -1 -1')