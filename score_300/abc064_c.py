N = int(input())
AB = list(map(int, input().split()))

c = 0
n = 0

for i in range(8):
    for j in AB:
        if 400*i <= j < 400*(i+1):
            c+=1
            break

for i in AB:
    if i >= 3200:
        n+=1

if c > 0:
    min = c
elif c == 0:
    min = 1
print(min,n+c)

