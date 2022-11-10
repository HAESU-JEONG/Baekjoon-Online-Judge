apt_person = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    apt_person[i][0] = 1

for i in range(14):
    apt_person[0][i] = i + 1

for i in range(15):
    for j in range(15):
        if i == 0:
            continue
        if j == 0:
            continue
        apt_person[i][j] = apt_person[i][j - 1] + apt_person[i-1][j]

test_case = int(input())
for i in range(test_case):
    input_i = int(input())
    input_j = int(input())
    print(apt_person[input_i][input_j - 1])