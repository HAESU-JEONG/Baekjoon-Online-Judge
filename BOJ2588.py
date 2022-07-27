num1 = int(input())
num2 = input()
num2_list = list(num2)
mul_list = []

for i in num2_list:
    mul_list.append(num1 * int(i))

for i in range(len(mul_list) - 1, -1, -1):
    print(mul_list[i])

print(num1 * int(num2))