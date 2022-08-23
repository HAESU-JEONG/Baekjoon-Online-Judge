number = int(input())
num_list = []
cnt = 0

if number < 10:
    num_list.append(0)
    num_list.append(number)

else:
    num_list = list(map(int, str(number)))

while True:
    cnt += 1
    sum_element = num_list[len(num_list) - 2] + num_list[len(num_list) - 1]

    if sum_element >= 10:
        sum_element = sum_element % 10

    num_list.append(sum_element)
    new_number = num_list[len(num_list) - 2] * 10 + num_list[len(num_list) - 1]

    if new_number == number:
        break

print(cnt)
