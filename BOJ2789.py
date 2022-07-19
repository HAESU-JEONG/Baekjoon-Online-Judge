list1 = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
string = input()

for i in range(len(list1)):
    string = string.replace(list1[i], "")

print(string)