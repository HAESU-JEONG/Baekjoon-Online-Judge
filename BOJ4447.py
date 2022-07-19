num = int(input())

for i in range(num):
    g = 0
    b = 0
    string = input()
    g += string.count('g')
    g += string.count('G')
    b += string.count('b')
    b += string.count("B")
    if g > b:
        print(string, "is GOOD")
    elif b > g:
        print(string, "is A BADDY")
    else:
        print(string, "is NEUTRAL")