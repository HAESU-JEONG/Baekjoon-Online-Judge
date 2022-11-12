sum_total, minus_total = map(int, input().split())

if sum_total < minus_total:
    print(-1)
else:
    x = (sum_total + minus_total) // 2
    y = (sum_total - minus_total) // 2

    if x + y == sum_total and x - y == minus_total:
        print(x, y)
    else:
        print(-1)