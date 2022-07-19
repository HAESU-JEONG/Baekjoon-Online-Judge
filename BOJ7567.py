string = list(input())

result = 10
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        result += 5
    else:
        result += 10
print(result)