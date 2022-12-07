while True:
    n = int(input())
    if n == -1:
        break
    
    num_list = []

    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)

    if sum(num_list) == n:
        print("{} = ".format(n), end = "")
        for i in range(len(num_list)):
            if i == len(num_list) - 1:
                print(num_list[i])
            else:
                print("{} + ".format(num_list[i]), end = "")
    else:
        print("{} is NOT perfect.".format(n))