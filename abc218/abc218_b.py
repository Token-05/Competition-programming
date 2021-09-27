P = list(map(int, input().split()))
moji = list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(moji)):
    print(moji[P[i]-1], end='')