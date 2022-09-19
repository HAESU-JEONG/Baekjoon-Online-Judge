n, m = map(int, input().split())
div_n = n // 2
div_m = m // 2

if n < m:
    print(div_n)
else:
    print(div_m)