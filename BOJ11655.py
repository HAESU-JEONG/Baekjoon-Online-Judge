string = list(input())

for i in range(len(string)):
    if ord(string[i]) >= 97 and ord(string[i]) <= 122:
        if ord(string[i]) + 13 > 122:
            temp = ord(string[i]) + 13 - 122 -1
            string[i] = chr(97 + temp)
        else:
            string[i] = chr(ord(string[i]) + 13)
    elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
        if ord(string[i]) + 13 > 90:
            temp = ord(string[i]) + 13 - 90 -1
            string[i] = chr(65 + temp)
        else:
            string[i] = chr(ord(string[i]) + 13)
    else:
        continue

print(''.join(string))