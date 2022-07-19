string = input()
for i in range(len(string)):
    if i == 0:
        print(string[i], end = "")
    if string[i] == '-':
        print(string[i + 1], end = "")