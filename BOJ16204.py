n, m, k = map(int, input().split())
O = n - m
X = n - k

if O > X:
    print(n - (O - X))
else:
    print(n - (X - O))