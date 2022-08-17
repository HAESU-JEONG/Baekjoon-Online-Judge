student_list = []

for i in range(28):
    student_list.append(int(input()))

for i in range(1, 31):
    if student_list.count(i) == 0:
        print(i)