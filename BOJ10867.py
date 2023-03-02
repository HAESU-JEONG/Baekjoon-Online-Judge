n = int(input())
num_list = list(map(int, input().split()))
set_num = list(set(num_list))
set_num.sort()
for num in set_num:
    print(num, end = " ")