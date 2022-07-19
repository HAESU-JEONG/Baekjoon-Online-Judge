list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    cnt = 0
    string = input()
    if string == '#':
        break
    for i in list1:
        cnt = cnt + string.count(i)
    print(cnt)