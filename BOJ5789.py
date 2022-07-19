num = int(input())
for i in range(num):
    string = list(input())
    check = True
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            check = False
        else:
            check = True
    if check == True:
        print("Do-it")
    else:
        print("Do-it-Not")