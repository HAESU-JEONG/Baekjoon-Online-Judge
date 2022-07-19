string = input()

happy = 0
sad = 0

if string.count(":-)") != -1:
    happy = string.count(":-)")
if string.count(":-(") != -1:
    sad = string.count(":-(")

if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad != 0 and happy != 0 and sad == happy:
    print("unsure")
else:
    print("none")