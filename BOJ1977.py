m = int(input())
n = int(input())
perfect_num = []

for i in range(m, n+1):
    if i ** (1/2) == int(i ** (1/2)):
        perfect_num.append(i)

result = sum(perfect_num)
if result == 0:
    print(-1)
else:
    print(result)
    print(perfect_num[0])