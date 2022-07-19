num = list(input())

first = 0
second = 0
for i in range(int(len(num) / 2)):
    first += int(num[i])
    second += int(num[int(len(num) - 1) - i])

if first == second:
    print("LUCKY")
else:
    print("READY")