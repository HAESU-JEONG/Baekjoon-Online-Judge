divide_num = []

for i in range(10):
    n = int(input())
    divide_num.append(n % 42)

print(len(set(divide_num)))