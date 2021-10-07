import copy

S = list(input())
N = list(input())
sa_len = len(S)-len(N)+1
temp = []

for i in range(sa_len):
    flag = 0
    for j in range(len(N)):
        if S[i+j] != N[j] and S[i+j] != '?': break
        flag += 1
    if flag == len(N):
        S1 = copy.copy(S)
        S1[i:len(N)+i] = N
        S_dush = ''.join(S1)
        t = S_dush.replace('?','a')
        temp.append(t)

if len(temp) == 0:
    print('UNRESTORABLE')
else:
    temp.sort()
    print(temp[0])