n = int(input())
charge = 1000 - n

answer = 0
coin_list = [500, 100, 50, 10, 5, 1]
coin = coin_list[0]
index = 0

while True:
    if charge >= coin:
        answer += 1
        charge -=  coin

        if charge == 0:
            print(answer)
            break
    else:
        index += 1
        coin = coin_list[index]