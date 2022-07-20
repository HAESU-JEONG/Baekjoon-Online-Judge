n, x = map(int, input().split())

number_list = list(input().split())

for i in range(n):
    if int(number_list[i]) < x:
        print(number_list[i], end=" ")