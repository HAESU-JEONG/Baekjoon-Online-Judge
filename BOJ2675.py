n = int(input())

for i in range(n):
    num, string = input().split()
    num = int(num)
    for index, value in enumerate(string):
        for j in range(num):
            print(value, end = "")
    print()