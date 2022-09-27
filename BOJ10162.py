n = int(input())

sec_list = [300, 60, 10]
button_list = [0, 0, 0]
sec = sec_list[0]
index = 0

while True:
    if n >= sec:
        button_list[index] += 1
        n -= sec
        if n == 0:
            print(button_list[0], button_list[1], button_list[2])
            break
    else:
        index += 1
        if index >= 3:
            print(-1)
            break
        sec = sec_list[index]