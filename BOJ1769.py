num = list(input())
temp_num = []
for i in range(len(num)):
    temp_num.append(int(num[i]))

total = 0
tm = []
idx = 0
cnt = 0

length = len(temp_num)
for i in range(length):
    total += temp_num[i]

if total < 10:
    print(cnt)
    if total % 3 == 0:
        print("YES")
    else:
        print("NO")

else:
    cnt = 1
    while True:
        tm = list(map(int, str(total)))
        idx = len(tm)
        total = 0
        for i in range(idx):
            total += tm[i]
        cnt += 1
        if total < 10:
            print(cnt)
            if total % 3 == 0:
                print("YES")
                break
            else:
                print("NO")
                break