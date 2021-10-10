N = int(input())
C,S,F = [0]*500,[0]*500,[0]*500
for i in range(N-1):
    law = list(map(int,input().split()))
    C[i],S[i],F[i] = law[0],law[1],law[2]

for i in range(N):
    t = 0
    for j in range(i,N-1):
        if t < S[j]: t = S [j]
        elif t % F [j]==0: pass
        else: t = t + F[j] - t % F[j]
        t += C [j]
    print(t)
