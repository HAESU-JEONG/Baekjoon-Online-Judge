mon = int(input())
day = int(input())

if mon == 2:
    if day == 18:
        print("Special")
    elif day < 18:
        print("Before")
    else:
        print("After")

elif mon > 2:
    print("After")

else:
    print("Before")