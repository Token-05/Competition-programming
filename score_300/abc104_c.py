import itertools

D, G = map(int, input().split())
pc = [map(int, input().split()) for _ in range(D)]
p, c = [list(i) for i in zip(*pc)]
count = sum = halfway = 0 #順に、解く問題数、それぞれの計算時点での得点、適当に説く問題のインデックス、を保持する変数
forlist = [list(e) for e in itertools.product([0, 1], repeat=D)]
res = []

for i in forlist:
    for jindex,j in enumerate(i):
        if j == 1:
            sum += 100 * (jindex+1) * p[jindex] + c[jindex]
            count += p[jindex]
        else: halfway = jindex
    if sum < G :
        for k in range(p[halfway]-1):
            sum += 100 * (halfway+1)
            count += 1
            if sum >= G:
                res.append(count)
                break
    else:
        res.append(count)
    count = sum = halfway = 0

print(min(res))