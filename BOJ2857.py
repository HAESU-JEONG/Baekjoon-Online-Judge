count = 0
list1 = []
list2 = []
for i in range(5):
    list1.append(input())

for i in range(5):
    if "FBI" in list1[i]:
        list2.append(i + 1)
        count += 1

if count == 0:
    print("HE GOT AWAY!")
else:
    for i in list2:
        print(i, end = " ")