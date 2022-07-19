string = list(input())
inputkey = list(input())
key = []

for i in range(len(inputkey)):
    key.append(ord(inputkey[i]) - 97)

k = 0
for i in range(len(string)):
    if k >= len(inputkey):
        k = 0

    if string[i] == ' ':
        k += 1
        print(" ", end = "")
        continue
    elif chr(ord(string[i])) == inputkey[k]:
        print("z", end="")
        k += 1
        continue
    elif ord(string[i]) - key[k] < 97:
        print(chr(ord(string[i]) - key[k] + 25), end = "")
        k += 1
        continue
    else:
        print(chr(ord(string[i]) - key[k] - 1), end = "")
        k += 1
        continue