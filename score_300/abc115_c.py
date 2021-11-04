N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
tmp = 10 ** 9

h.sort()

for i in range(N-K+1):
    hrate = h[i+K-1] - h[i]
    if hrate <= tmp: tmp = hrate

print(tmp)