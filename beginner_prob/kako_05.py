# 5. ABC 083 B - Some Sums
s = list(map(int,input().split(" ")))
N = s[0]
A = s[1]
B = s[2]
mylist = []
for i in range(1,N+1):
    cha = str(i)
    array = list(map(int, cha))
    t = sum(array)
    if(A <= t and t <= B):
        mylist.append(i)
print(sum(mylist))