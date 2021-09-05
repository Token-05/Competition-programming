# 1. ABC 086 A - Product
a, b = map(int, input().split(" "))
if(a*b %2 == 0):
    print("Even")
else:
    print("Odd")