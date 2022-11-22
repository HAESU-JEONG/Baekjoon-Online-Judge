n = int(input())
for i in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        print("Scenario #{}:".format(i + 1))
        print("yes")
    else:
        print("Scenario #{}:".format(i + 1))
        print("no")
    print()