num_list = list(map(int, input().split()))

ascending_list = [1, 2, 3, 4, 5, 6, 7, 8]
descending_list = [8, 7, 6, 5, 4, 3, 2, 1]

ascending_check = 0
descending_check = 0

for i in range(8):
    if num_list[i] == descending_list[i]:
        descending_check = descending_check + 1
    elif num_list[i] == ascending_list[i]:
        ascending_check = ascending_check + 1

if ascending_check == 8:
    print("ascending")

elif descending_check == 8:
    print("descending")

else:
    print("mixed")