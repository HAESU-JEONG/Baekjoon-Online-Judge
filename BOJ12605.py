num = int(input())

for i in range(num):
    string = list(input().split())
    print("Case #{}:".format(i+ 1), end = " ")
    for j in range(len(string) - 1, -1, -1):
        print(string[j], end = " ")
    print()