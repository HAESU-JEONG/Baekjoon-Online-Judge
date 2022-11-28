while True:
    string = list(input())
    if ''.join(string) == "***":
        break

    reverse_string = reversed(string)
    print(''.join(list(reverse_string)))