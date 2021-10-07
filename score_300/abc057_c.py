N = int(input())

def make_divisors(n):
    lower_divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(max(len(str(i)),len(str(n//i))))
        i += 1
    return lower_divisors

if __name__ == '__main__':
    print(make_divisors(N)[-1])