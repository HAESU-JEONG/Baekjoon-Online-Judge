def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    print(lcm(a, b))