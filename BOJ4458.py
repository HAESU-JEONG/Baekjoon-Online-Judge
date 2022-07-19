num = int(input())

for i in range(num):
    string = input()
    if ord(string[0]) >= 97:
        new_string = string[0].replace(string[0], chr(ord(string[0]) - 32))
        print(new_string, end = "")
        for j in range(1, len(string)):
            print(string[j], end = "")
        print()
    else:
        print(string)