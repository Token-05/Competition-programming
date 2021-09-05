# 6. ABC 088 B - Card Game for Two
N = int(input())
s = list(map(int,input().split(" ")))
s.sort()
Alice = 0
Bob = 0
for i in s:
    if N % 2 == 1:
        Alice += i
    else:
        Bob += i
    N -= 1
print(Alice-Bob)