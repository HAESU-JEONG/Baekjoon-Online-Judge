n = int(input())
price  = int(input())
sales = [0]

if n >= 5:
    sales.append(500)
if n >= 10:
    sales.append(price // 10)
if n >= 15:
    sales.append(2000)
if n >= 20:
    sales.append(price // 4)

result = price - max(sales)
if result < 0:
    print(0)
else:
    print(result)