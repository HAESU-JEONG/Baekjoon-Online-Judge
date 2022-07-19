num = int(input())

for i in range(num, 0, -1):
    for j in range(num, 0, -1):
        if i == j:
            print("*" * i, end = "")
            break
        print(" ", end = "")
    print()