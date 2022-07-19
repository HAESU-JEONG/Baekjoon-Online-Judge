while True:
    try:
        string = input()
        low = 0
        upp = 0
        num = 0
        blank = 0

        for i in range(len(string)):
            if string[i].islower():
                low += 1
            if string[i].isupper():
                upp += 1
            if string[i].isdecimal():
                num += 1
            if string[i].isspace():
                blank += 1

        print(low, upp, num, blank)
    except EOFError:
        break