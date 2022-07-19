A = int(input())
B = int(input())
C = int(input())

multiply = list(str(A * B * C))
number_list = [0 for i in range(10)]

for i in range(len(multiply)):
    for j in range(len(number_list)):
        if multiply[i] == str(j):
            number_list[j] += 1
            break

for i in range(len(number_list)):
    print(number_list[i])