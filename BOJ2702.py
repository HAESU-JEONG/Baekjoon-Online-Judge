import sys

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    result = (x*y)//gcd(x, y)
    return result

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b), end=" ")
    print(gcd(a, b))