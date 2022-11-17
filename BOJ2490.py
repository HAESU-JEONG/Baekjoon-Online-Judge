for i in range(3):
    num_list = list(map(int, input().split()))
    cnt = num_list.count(0)
    if cnt == 4:
        print("D")
    elif cnt == 3:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 1:
        print("A")
    else:
        print("E")