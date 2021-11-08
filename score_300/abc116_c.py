N = int(input())
h = list(map(int,input().split()))
before, count = 0, 0

while sum(h) != 0:
    for i in range(N):
        if h[i] == 0 and before < i:
            mini = min(h[before:i])
            length = len(h[before:i])
            for j in range(length):
                h[before+j] -= mini
            count += mini
        elif h[before] == 0: 
            before += 1

    mini = min(h[before:])
    length = len(h[before:])
    for j in range(length):
        h[before+j] -= mini
    before = 0
    count += mini

print(count)