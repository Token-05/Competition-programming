N = int(input())

p = N
for i in range(N):
    cc = 0
    t = i
    while (t >0):
        cc += t % 6
        t = t // 6
    t=N - i
    while (t >0):
        cc += t % 9
        t = t // 9
    if p > cc:
        p = cc
    print(p)

print(p)