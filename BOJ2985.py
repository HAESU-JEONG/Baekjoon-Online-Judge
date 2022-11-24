num1, num2, num3 = map(int, input().split())

if num1 + num2 == num3:
    print("{}+{}={}".format(num1, num2, num3))
elif num1 - num2 == num3:
    print("{}-{}={}".format(num1, num2, num3))
elif num1 * num2 == num3:
    print("{}*{}={}".format(num1, num2, num3))
elif num1 // num2 == num3:
    print("{}/{}={}".format(num1, num2, num3))
elif num2 + num3 == num1:
    print("{}={}+{}".format(num1, num2, num3))
elif num2 - num3 == num1:
    print("{}={}-{}".format(num1, num2, num3))
elif num2 * num3 == num1:
    print("{}={}*{}".format(num1, num2, num3))
elif num2 // num3 == num1:
    print("{}={}/{}".format(num1, num2, num3))