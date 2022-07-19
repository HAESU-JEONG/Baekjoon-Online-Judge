num1, num2 = input().split()

reverse_num1 = list(reversed(num1))
reverse_num2 = list(reversed(num2))

if int(''.join(reverse_num1)) > int(''.join(reverse_num2)):
    print(int(''.join(reverse_num1)))

else:
    print(int(''.join(reverse_num2)))
