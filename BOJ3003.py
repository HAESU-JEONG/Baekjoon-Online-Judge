num_list = list(map(int, input().split()))
standard = [1, 1, 2, 2, 2, 8]

for i in range(len(num_list)):
    print(standard[i] - num_list[i], end = " ")