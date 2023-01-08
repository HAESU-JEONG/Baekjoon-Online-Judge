num = int(input())
num_list = []
for _ in range(num):
    x, y = map(int, input().split())
    num_list.append([y, x])

num_list.sort()

for i in range(num):
    print(num_list[i][1], num_list[i][0])