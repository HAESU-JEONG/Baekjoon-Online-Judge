n = int(input())

str = [[0 for i in range(80)] for j in range(n)]

for i in range(n):
    str[i] = input()
    score = 0
    total = 0
    for j in range(len(str[i])):
        if str[i][j] == "O":
            score = score + 1
            total = total + score
        else:
            score = 0
        
    print(total)