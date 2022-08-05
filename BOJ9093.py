t = int(input())

for i in range(t):
    input_list = list(input().split())
    string_input_data = []

    for j in range(len(input_list)):
        result = list(input_list[j])
        print(''.join(result[::-1]), end = " ")
    print()