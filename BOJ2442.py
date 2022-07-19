num = int(input())

for i in range(num):
    for j in range(num, 0, -1):
        if i + j == num - 1:
            print(" " * j, end = "")
            break
    print("*" * (2 * i + 1), end = "")
    print()