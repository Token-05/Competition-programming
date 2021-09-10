h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
flag = True
for i in range(h):
    for j in range(w):
        cnt = 0
        if i>=1 and field[i-1][j] == ".":
            cnt += 1
        if i<h-1 and field[i+1][j] == ".":
            cnt += 1
        if j>=1 and field[i][j-1] == ".":
            cnt += 1
        if j<w-1 and field[i][j+1] == ".":
            cnt += 1
        if field[i][j] == "#" and cnt > 3:
            print("No")
            flag = False
            break
    else:
        continue
    break
if flag:
    print("Yes")