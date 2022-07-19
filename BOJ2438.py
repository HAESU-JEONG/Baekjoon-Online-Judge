num = int(input())

for i in range(num):
    for j in range(num):
        print("*", end = "")
        if i == j:
            break
    print()