seven_price, seven_gram = map(int, input().split())
n = int(input())
convenience_store = [[0] * 2] * n
convenience_price = [0] * (n + 1)

for i in range(n):
    convenience_store[i][0], convenience_store[i][1] = map(int, input().split())
    convenience_price[i] = convenience_store[i][0] / convenience_store[i][1]
convenience_price[-1]= seven_price / seven_gram

print("{:.2f}".format(min(convenience_price) * 1000))