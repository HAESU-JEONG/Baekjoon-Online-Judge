while True:
    num_list = list(map(int, input().split()))

    if num_list[0] == 0 and num_list[1] == 0 and num_list[2] == 0:
        break
    num_list.sort()

    if num_list[2] >= num_list[0] + num_list[1]:
        print("Invalid")
        continue
    if num_list[0] == num_list[1] and num_list[1] == num_list[2]:
        print("Equilateral")
    elif num_list[0] == num_list[1] or num_list[1] == num_list[2]:
        print("Isosceles")
    else:
        print("Scalene")