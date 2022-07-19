string = input()
list1 = []

for i in range(len(string)):
    list1.append(string[i:])

list1.sort()

for i in list1:
    print(i)