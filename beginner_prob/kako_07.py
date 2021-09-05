# 7. ABC 085 B - Kagami Mochi
N = int(input())
s = [int(input()) for i in range(N)]
flag = 0
for i in range(0, 101):
    if s.count(i) > 0:
        flag += 1
print(flag)