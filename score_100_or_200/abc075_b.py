# 脳筋アルゴリズム
H,W = map(int,input().split(" "))
zero = [['.']*(W+2)]
A = zero + [['.']+[c for c in input()]+['.'] for i in range(H)] + zero
for j in range(0,H+2):
    for i in range(0,W+2):
        if '.' in A[j][i]:
            A[j][i] = A[j][i].replace('.','0')
        elif '#' in A[j][i]:
            A[j][i] = A[j][i].replace('#','9')
A = [[int(x) for x in y] for y in A]
for j in range(1,H+2):
    for i in range(1,W+2):
        if 8 < A[j][i]:
            A[j][i+1] += 1
            A[j+1][i+1] += 1
            A[j+1][i] += 1
            A[j+1][i-1] += 1
            A[j][i-1] += 1
            A[j-1][i-1] += 1
            A[j-1][i] += 1
            A[j-1][i+1] += 1
for j in range(1,H+1):
    for i in range(1,W+1):
        if 8 < A[j][i]:
            A[j][i] = '#'
        print(A[j][i], end='')
    print()
# こちらが3倍も早いアルゴリズム
# h, w = map(int, input().split())
# field = [list(input()) for _ in range(h)]
# for i in range(h):
#     for j in range(w):
#         cnt = 0
#         if i>=1 and field[i-1][j] == "#":
#             cnt += 1
#         if i<h-1 and field[i+1][j] == "#":
#             cnt += 1
#         if j>=1 and field[i][j-1] == "#":
#             cnt += 1
#         if j<w-1 and field[i][j+1] == "#":
#             cnt += 1
#         if i>=1 and j>=1 and field[i-1][j-1] == "#":
#             cnt += 1
#         if i<h-1 and j<w-1 and field[i+1][j+1] == "#":
#             cnt += 1
#         if i >= 1 and j<w-1 and field[i-1][j+1] == "#":
#             cnt += 1
#         if i<h-1 and j>=1 and field[i+1][j-1] == "#":
#             cnt += 1
#         if field[i][j] == ".":
#             field[i][j] = str(cnt)
# for f in field:
#     f = "".join(f)
#     print(f)
# 上のコードは見方を変えたことによる弊害であり気をつけるべき