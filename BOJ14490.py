n, m = map(int, input().split(":"))

from math import gcd
num = gcd(n, m)

print(f"{n // num}:{m // num}")