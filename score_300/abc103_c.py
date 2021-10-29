# Python3.9以降の標準機能であるmath.lcm()は使えないので自作する必要がある

from math import gcd

def lcm(a):
    cc = a[0]
    for index in range(len(a)-1):
        cc = cc//gcd(cc,a[index+1])*a[index+1]
    return cc

def main():
    N = int(input())
    a = list(map(int,input().split()))
    lcms = lcm(a) - 1
    cnt = 0
    for i in a:
        if i == 0 : pass
        else : cnt += lcms % i
    print(cnt)

if __name__ == '__main__':
    main()