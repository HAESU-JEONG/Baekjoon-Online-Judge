num_list = list(map(int, input().split()))
ordering_list = list(input())

num_list.sort()

for order in ordering_list:
    if order == 'A':
        print(num_list[0], end=" ")
    elif order == 'B':
        print(num_list[1], end=" ")
    else:
        print(num_list[2], end=" ")