num = int(input())
string = []
for i in range(num):
    string.append(input())

set_string = set(string)
string.sort()
sort_set = []
sort_set = sorted(set_string)

count = [0 for i in range(len(set_string))]

for i in range(len(set_string)):
    count[i] = string.count(list(sort_set)[i])

max = 0
index = 0
for idx, value in enumerate(count):
    if max < value:
        max = value
        index = idx

print(list(sort_set)[index])