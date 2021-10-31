# 2進法を求める方法と実に同じ

N = int(input())
binary = ""

while N != 0:
    mod = N % (-2)
    if mod < 0 : mod = -mod
    N = (N - mod) / (-2)
    binary += str(int(mod))

if binary == "": binary = "0"
print(binary[::-1]) # 反転