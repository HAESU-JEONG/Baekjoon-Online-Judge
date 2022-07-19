string = input()
alpha = [0 for i in range(26)]

for i in range(len(string)):
    alpha[ord(string[i]) - 97] += 1

for i in alpha:
    print(i, end = " ")