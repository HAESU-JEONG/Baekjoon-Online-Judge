t = int(input())

for i in range(t):
    string_list = list(input())

    if len(string_list) == 1:
        print(string_list[0], end="")
        print(string_list[0])
    
    else:
        print(string_list[0], end="")
        print(string_list[len(string_list) - 1])