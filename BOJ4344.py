c = int(input())

for i in range(c):
    num_list = list(map(int, input().split()))
    avg_list = []

    for i in range(1, num_list[0] + 1):
        avg_list.append(num_list[i])
    
    avg_result = sum(avg_list) / len(avg_list)
    upper_cnt = 0

    for i in range(len(avg_list)):
        if avg_list[i] > avg_result:
            upper_cnt += 1
    
    result = upper_cnt / len(avg_list) * 100
    print('%.3f%%' % round(result, 3))