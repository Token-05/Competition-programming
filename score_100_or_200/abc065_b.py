N = int(input())
A = [int(input()) for i in range(N)]
a_index = 0
cnt = 0
while cnt < N+1:
    cnt += 1
    a_index = A[a_index] - 1
    if a_index == 1:
        print(cnt)
        break
if cnt == N+1:
    print(-1)