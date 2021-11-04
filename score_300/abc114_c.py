import itertools

r, sum = [], 0
N = int(input())
for list in [list(e) for e in itertools.product('0357', repeat=len(str(N)))]:
    r.append(int(''.join(list)))

for k in r:
    f = str(k)
    t = f.count('3') + f.count('5') + f.count('7')
    if '3' in f and '5' in f and '7' in f and t == len(f) and N >= k:
        sum += 1

print(sum)