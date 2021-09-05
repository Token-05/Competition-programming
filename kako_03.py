# 3. ABC 081 B - Shift Only
N = int(input())
s = list(map(int,input().split(" ")))
def test(value):
    j = 0
    while value % 2 == 0:
        value /= 2
        j += 1
    return j
l = list(map(test, s))
print(min(l))