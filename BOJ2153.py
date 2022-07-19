string = input()
alpha = [0] * 52

for i in range(len(string)):
    if string[i].islower():
        alpha[ord(string[i]) - 97] += 1
    else:
        alpha[ord(string[i]) - 65 + 26] += 1

total = 0
for i in range(52):
    if alpha[i] != 0:
        total += (i + 1) * alpha[i]

check = True

for i in range(2, total):
    if total % i == 0:
        check = False
        break

if check == False:
    print("It is not a prime word.")
else:
    print("It is a prime word.")