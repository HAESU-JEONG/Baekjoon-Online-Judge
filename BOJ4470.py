n = int(input())
number_list = []

for i in range(n):
    number_list.append(input())

for index in range(n):
    print(index + 1, end="")
    print(".", end = " ")
    print(number_list[index])