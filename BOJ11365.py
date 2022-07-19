while True:
    string = list(input().split())

    if ''.join(string) == "END":
        break
    else:
        for i in range(len(string)):
            print(''.join(reversed(string[len(string) - 1 -i])), end = " ")
    print()