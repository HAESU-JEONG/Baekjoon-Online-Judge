num = int(input())

for i in range(num, 0, -1):
    for j in range(num, 0, -1):
        if i + j == num:
            print(" " * j, end = "")
            break
    print("*" * (2 * i - 1), end = "")
    print()