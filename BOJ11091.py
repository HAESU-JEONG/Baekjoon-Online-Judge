num = int(input())

for i in range(num):
    alpha = [0]*26
    string = input()
    string2 = string.lower()
    for j in range(len(string2)):
        if ord(string2[j]) >= 97 and ord(string2[j]) <= 122:
            alpha[ord(string2[j]) - 97] += 1
    check = False
    list1 = []
    for i in range(26):
        if alpha[i] == 0:
            list1.append(i)
            check = True

    if check == True:
        print("missing", end = " ")
        for i in list1:
            print(chr(i + 97), end = "")
        print()
    else:
        print("pangram")