# law = 0
# for i in range(3):
#     law += sum(list(map(int,input().split())))

# if law % 3 == 0:print('Yes')
# else:print('No')

N = 3
C = [list(map(int,input().split())) for _ in range(N)]

a,b = [0]*3,[0]*3
flag = False
for k in range(0,C[0][0]+1):
    a1 = k
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1
    if C[1][0] - b1 == C[1][1] - b2 == C[1][2] - b3:
        a2 = C[1][0] - b1
    else:continue
    if C[2][0] - b1 == C[2][1] - b2 == C[2][2] - b3:
        a3 = C[2][0] - b1
        flag = True
        break
    else:continue

if flag:print('Yes')
else:print('No')