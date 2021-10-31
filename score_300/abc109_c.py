import math

N, X = map(int, input().split())
x = list(map(int,input().split()))
tmp = abs(X-x[0])

for i in range(N-1):
    tmp = math.gcd(tmp,abs(X-x[i+1]))

print(tmp)