while True:
    num = input()
    if num == '0':
        break

    rnum = ''.join(reversed(num))

    if num == rnum:
        print("yes")
    else:
        print("no")