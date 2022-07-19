cal1, cal2 = list(input().split())
first = 0
second = 0
for i in range(len(cal1)):
    first += int(cal1[i])
for j in range(len(cal2)):
    second += int(cal2[j])
print(first * second)