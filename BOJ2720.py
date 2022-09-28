test_case = int(input())
money_list = []

for i in range(test_case):
    money_list.append(int(input()))

coin_list = [25, 10, 5, 1]
coin = coin_list[0]
money_index = 0
coin_index = 0

coin_count = [0] * 4

while True:
    if money_list[money_index] >= coin:
        coin_count[coin_index] += 1
        money_list[money_index] -= coin

        if money_list[money_index] == 0:
            print(coin_count[0], coin_count[1], coin_count[2], coin_count[3])
            money_index += 1
            coin = coin_list[0]
            coin_index = 0
            coin_count[0] = 0
            coin_count[1] = 0
            coin_count[2] = 0
            coin_count[3] = 0

            if money_index >= test_case:
                break
        
    else:
        coin_index += 1
        coin = coin_list[coin_index]