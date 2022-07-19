num = int(input())
for i in range(num):
    string = input()
    if string == "P=NP":
        print("skipped")
    else:
        string2 = list(string.split('+'))
        print(int(string2[0]) + int(string2[1]))