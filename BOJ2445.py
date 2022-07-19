num = int(input())

for i in range(num):
    print("*" * (i + 1), end = "")

    for j in range(num, 0, -1):
        if i + j == num - 1:
            print(" " * (2 * j), end = "")
    
    print("*" * (i + 1), end = "")
    print()

for i in range(num - 1, 0, -1):
    print("*" * i, end = "")

    for j in range(num):
        if i + j == num:
            print(" " * (2 * j), end = "")
    print("*" * i, end = "")
    print()