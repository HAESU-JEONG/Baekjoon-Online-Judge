string = input()
string_list = list(string)
rstring = ''.join(reversed(string))

if string == rstring:
    print(1)
else:
    print(0)