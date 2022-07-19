num = int(input())
string = []

for i in range(num):
    string.append(input())

string2 = set(string)
string2 = list(string2)
string2.sort()
string2.sort(key=len)

for i in string2:
    print(i)