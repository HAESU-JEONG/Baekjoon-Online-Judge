string1 = list(input())
string2 = list(input())

for i in range(len(string1)):
    for j in range(len(string2)):
        if string2[j] == string1[i]:
            string2[j] = -1
            string1[i] = -1
            break

if string2.count(-1) == len(string2):
    print(1)
else:
    print(0)