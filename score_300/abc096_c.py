H, W = map(int,input().split())
C = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if '#' in C[i][j]:
            for k in [1,0],[0,-1],[-1,0],[0,1]:
                if 0 <= j+k[0] < W and 0 <= i+k[1] < H and '#' in C[i+k[1]][j+k[0]]:
                    break   
            else:
                print("No")
                exit()

print('Yes')
