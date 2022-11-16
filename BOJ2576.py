num_list = []
odd_list = []

for i in range(7):
    num_list.append(int(input()))

for num in num_list:
    if num % 2 == 1:
        odd_list.append(num)

sum_result = sum(odd_list)

if sum_result == 0:
    print(-1)
else:
    print(sum_result)
    print(min(odd_list))