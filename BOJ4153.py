while True:
    num_list = list(map(int, input().split()))

    if num_list.count(0) == 3:
        break

    num_list.sort()

    if num_list[2] == (num_list[0]**2 + num_list[1]**2)**0.5:
        print("right")
    else:
        print("wrong")