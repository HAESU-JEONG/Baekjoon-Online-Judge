num = int(input())

for i in range(num):
    result = 0
    alpha = [0] * 26
    string = list(input())
    for j in range(len(string)):
        alpha[ord(string[j]) - 65] += 1
    for j in range(26):
        if alpha[j] == 0:
            result += j + 65
    print(result)