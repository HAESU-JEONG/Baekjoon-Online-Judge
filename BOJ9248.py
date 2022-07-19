string = input()
di = {}
for i in range(len(string)):
    di[string[i:]] = i + 1

di2 = sorted(di.items())
list1 = []
for idx, value in di2:
    print(value, end = " ")
    list1.append(idx)
print()

list2 = ['x']
for i in range(1, len(list1)):
    cnt = 0
    for j in range(len(list1[i])):
        if j > len(list1[i - 1]) - 1:
            break
        if list1[i - 1][j] == list1[i][j]:
            cnt += 1
        if j == 0 and cnt == 0:
            break
        if j + 1 != cnt:
            break
    list2.append(cnt)

for i in list2:
    print(i, end = " ")