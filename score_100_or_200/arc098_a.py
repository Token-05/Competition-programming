# ./arc098_a_detail.pdf
N = int(input())
S = list(input())
ans = S.count("E")
tmp = ans
for i in range(N):
    if S[i] == "E":
        tmp -= 1
    if S[i] == "W":
        tmp += 1
    ans = min(ans, tmp) #最小の値を保持
print(ans)