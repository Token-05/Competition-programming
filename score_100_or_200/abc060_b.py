a, b, c = map(int, input().split())
flag = True
for i in range(0,10000): # 10000はかなり適当
    if (b * i + c) % a == 0:
        print("YES")
        flag = False
        break
if flag:
    print("NO")
