n = int(input())

for i in range(n):
    password_length = len(input())
    if password_length >= 6 and password_length <= 9:
        print("yes")
    else:
        print("no")