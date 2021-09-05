# 8. ABC 085 C - Otoshidama
N,Y = map(int,input().split(" "))
first_paper = -1
second_paper = -1
third_paper = -1
for a in range(0,N+1):
    for b in range(0,N-a+1):
        c = N - a - b
        sum = 10000*a + 5000*b + 1000*c
        if sum == Y :
            first_paper = a
            second_paper = b
            third_paper = c
print(first_paper, second_paper, third_paper)