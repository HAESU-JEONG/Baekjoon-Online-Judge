n = int(input())
num_list = list(map(int, input().split()))
cnt = 0

for num in num_list:
    check = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check = check + 1
            
        if check == 0:
            cnt = cnt + 1

print(cnt)
        