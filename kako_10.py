# 10. ABC 086 C - Traveling
N = int(input())
s = [[0,0,0]]
s.extend([list(map(int,input().split(" "))) for i in range(N)])
password = 'Yes'
for i in range(1,N+1):
    t_now, x_now, y_now, t_old, x_old, y_old = s[i][0], s[i][1], s[i][2], s[i-1][0], s[i-1][1], s[i-1][2]
    time = t_now - t_old
    x = abs(x_now - x_old)
    y = abs(y_now - y_old)
    distance = x + y
    if time >= distance and (time - distance) % 2 == 0:
        pass
    else:
        password = 'No'
        break
print(password)