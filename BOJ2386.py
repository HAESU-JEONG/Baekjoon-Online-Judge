while True:
    string = list(input().split())
    if string[0] == '#':
        break
    total = 0
    for i in range(1, len(string)):
        string2 = string[i].lower()
        total += string2.count(string[0])

    print(string[0], total)