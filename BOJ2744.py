string = list(input())

for i in range(len(string)):
    if ord(string[i]) >= 97 and ord(string[i]) <= 122:
        string[i] = chr(ord(string[i]) - 32)
    else:
        string[i] = chr(ord(string[i]) + 32)

print(''.join(string))