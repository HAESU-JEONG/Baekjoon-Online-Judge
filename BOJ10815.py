def binary_search(number_list, num, low, high):
    middle = 0
    if low < high or low == high:
        middle = (low + high) // 2;
        if num == number_list[middle]:
            return middle
        elif num < number_list[middle]:
            return binary_search(number_list, num, low, middle - 1)
        else:
            return binary_search(number_list, num, middle + 1, high)
    return -1

n = int(input())
number_card = list(map(int, input().split()))
m = int(input())
integer_list = list(map(int, input().split()))

number_card.sort()

for i in integer_list:
    idx = binary_search(number_card, i, 0, len(number_card) - 1)

    if idx != -1:
        print(1, end=" ")
    else:
        print(0, end=" ")