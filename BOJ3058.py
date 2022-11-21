t = int(input())
num_list = []
for i in range(t):
    num_list.append(list(map(int, input().split())))

for i in range(t):
    sum_total = 0
    min_num = 101
    for j in range(7):
        if num_list[i][j] % 2 == 0:
            sum_total += num_list[i][j]
            if min_num > num_list[i][j]:
                min_num = num_list[i][j]
    print(sum_total, min_num)