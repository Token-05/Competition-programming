N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

def plus():
    llen = 0
    for i in sorted(AB):
        llen += i[1]
        if llen >= K:
            return i[0]

print(plus())