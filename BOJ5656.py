i = 1
while True:
    num1, c, num2 = input().strip().split()
    if c == 'E':
        break
    else:
        if c == '>':
            if int(num1) > int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
        elif c == ">=":
            if int(num1) >= int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
        elif c == '<':
            if int(num1) < int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
        elif c == "<=":
            if int(num1) <= int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
        elif c == "==":
            if int(num1) == int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
        elif c == "!=":
            if int(num1) != int(num2):
                print("Case ", i, ": true")
            else:
                print("Case ", i, ": false")
    i += 1