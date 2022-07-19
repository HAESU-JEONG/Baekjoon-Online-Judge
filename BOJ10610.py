num = input()
num = sorted(num, reverse = True)
sum = 0

if '0' not in num:
    print(-1)
else:
    for i in num:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(num))