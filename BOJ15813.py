length = int(input())
string = input()

alpha = [0]*26

for i in range(len(string)):
    alpha[ord(string[i]) - 65] += 1
total = 0
for i in range(26):
    total += (i + 1) * alpha[i]
print(total)