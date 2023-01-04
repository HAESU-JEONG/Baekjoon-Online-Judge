string1 = input()
string2 = input()

string1_len = len(string1)
string2_len = len(string2)

if string1 * string2_len == string2 * string1_len:
    print(1)
else:
    print(0)