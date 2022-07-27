def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

num1, num2 = map(int, input().split())

divisor = gcd(num1, num2)
multiple = lcm(num1, num2)

print(divisor)
print(int(multiple))