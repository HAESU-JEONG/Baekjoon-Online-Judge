num = int(input())

for i in range(num):
    num2 = int(input())
    max = 0
    nname = ""
    for j in range(num2):
        n, name = input().split()
        num = int(n)
        if num > max:
            max = num
            nname = name
    print(nname)