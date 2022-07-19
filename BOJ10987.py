string = input()
list1 = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(len(string)):
    if string[i] in list1:
        count += 1

print(count)