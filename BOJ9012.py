num = int(input())

list1 = []

for i in range(num):
    string = list(input())
    prev = ""
    chk = 0
    for j in range(len(string)):
        if string[j] == '(':
            list1.append(string[j])
        else:
            if (not list1) == True:
                chk = 1
                break
            prev = list1.pop()
            if string[j] == ')' and prev != '(':
                chk = 1
                break
    if ((not list1) == True) or chk == 1:
        print("NO")
    else:
        print("YES")