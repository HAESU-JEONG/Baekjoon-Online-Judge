number_list = []

for i in range(9):
    n = int(input())
    number_list.append(n)

print(max(number_list))
print(number_list.index(max(number_list)) + 1)