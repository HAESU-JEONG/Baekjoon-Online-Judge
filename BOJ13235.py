string = input()
string2 = reversed(list(string))

if string == ''.join(string2):
    print("true")
else:
    print("false")