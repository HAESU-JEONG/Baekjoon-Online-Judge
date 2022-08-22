n = int(input())
coordinate_list = []

for i in range(n):
    x, y = map(int, input().split())
    coordinate_list.append([x, y])

coordinate_list.sort()

for i in range(len(coordinate_list)):
    print(coordinate_list[i][0], coordinate_list[i][1])