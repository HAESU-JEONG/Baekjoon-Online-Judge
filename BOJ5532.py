import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

kor = math.ceil(A / C)
mat = math.ceil(B / D)

max_day = max(kor, mat)

print(L - max_day)