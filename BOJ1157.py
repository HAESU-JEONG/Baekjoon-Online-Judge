string = input().lower()
stringList = list(set(string))

cnt = []

for i in stringList:
    count = string.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(stringList[(cnt.index(max(cnt)))].upper())