string1 = input()
string2 = input()

cnt = 0
n = 0
while n <= len(string1) - len(string2):
    if string1[n:n + len(string2)] == string2:
        cnt += 1
        n += len(string2)

    else:
        n += 1 
print(cnt)