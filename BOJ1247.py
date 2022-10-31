import sys

for i in range(3):
    test = int(sys.stdin.readline().rstrip())
    test_number = []
    for i in range(test):
        test_number.append(int(sys.stdin.readline().rstrip()))
    result = sum(test_number)
    if result == 0:
        print(0)
    elif result < 0:
        print("-")
    else:
        print("+")