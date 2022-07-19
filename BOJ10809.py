str = input()

alpha = [-1 for i in range(26)]

for index, value in enumerate(str):
    if alpha[ord(value) - 97] == -1:
        alpha[ord(value) - 97] = index

for i in range(26):
    print(alpha[i], end=" ")