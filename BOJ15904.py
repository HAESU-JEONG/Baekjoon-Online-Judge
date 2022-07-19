string = input()

list1 = ['U', 'C', 'P', 'C']
cnt = 0
for i in range(len(list1)):
    if list1[i] in string:
        index = string.find(list1[i])
        string = string[index:]
        cnt += 1

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")