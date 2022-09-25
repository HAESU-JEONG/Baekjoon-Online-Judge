a, b = map(int, input().split())
c = a * (b / 100)

if a - c >= 100:
    print(0)
else:
    print(1)