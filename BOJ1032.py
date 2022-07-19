num = int(input())
first = list(input())
length = len(first)
for i in range(num - 1):
    second = list(input())
    for j in range(length):
        if first[j] != second[j]:
            first[j] = '?'
print(''.join(first))