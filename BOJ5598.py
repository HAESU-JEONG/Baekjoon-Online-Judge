string = input()
strlist = list(string)

for i in strlist:
    if ord(i) - 3 < 65:
        print(chr(ord(i) -3 + 26), end = "")

    else:
        print(chr(ord(i) -3), end = "")