A, B = map(int, input().split())
P = B - A
Q = B

if Q % P == 0:
    print(P // P, end = " ")
    print(Q // P)
else:
    print(P, Q)