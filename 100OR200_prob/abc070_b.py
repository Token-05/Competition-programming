A, B, C, D = map(int, input().split())
max = A if A >= C else C
min = B if B <= D else D
print(min - max if min >= max else 0)