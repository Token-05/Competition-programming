# 4. ABC 087 B - Coins
s = list(int(input()) for i in range(4))
A = s[0]
B = s[1]
C = s[2]
X = s[3]
res = 0
for i in range(0,A+1):
    for j in range(0,B+1):
        for k in range(0,C+1):
            total = 500*i + 100*j + 50*k
            if (total == X):
                res += 1
print(res)