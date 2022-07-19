string = input()

for index, value in enumerate(string):
    if (index+1) % 10 == 0:
        print(value)
    else:
        print(value, end = "")
