list1 = [['*' for i in range(15)] for j in range(5)]

for i in range(5):
    string = list(input())
    length = len(string)

    for j in range(length):
        list1[i][j] = string[j]

list2 = []
for i in range(15):
    for j in range(5):
        list2.append(list1[j][i])

for i in list2:
    if i != '*':
        print(i, end = "")