import sys

n = int(sys.stdin.readline().rstrip())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

sort_num_list = sorted(num_list)

for i in range(n):
    print(sort_num_list[i])