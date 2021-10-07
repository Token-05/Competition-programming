def main():
    sx,sy,tx,ty = map(int, input().split())
    x,y,list = tx-sx,ty-sy,[]
    list.extend(['U'*y+'R'*x+'D'*y+'L'*(x+1)+'U'*(y+1)+'R'*(x+1)+'DR'+'D'*(y+1)+'L'*(x+1)+'U'])
    print(list[0])

if __name__ == '__main__':
    main()