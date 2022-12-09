t = int(input())
for _ in range(t):
    n = int(input())
    result = 1
    for i in range(1, n+1):
        result *= i
    num_string = list(str(result))
    
    for i in range(len(num_string)):
        if num_string[len(num_string) - 1 - i] == '0':
            continue
        else:
            print(num_string[len(num_string) - 1 - i])
            break