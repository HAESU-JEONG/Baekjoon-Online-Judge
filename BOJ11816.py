def change(string):
    if "0x" in string:
        num = int(string, 16)
        return num
    elif '0' == string[0]:
        num = int(string, 8)
        return num
    else:
        num = int(string)
        return num

string = input()
print(change(string))